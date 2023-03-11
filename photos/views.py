from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View, ListView
from django.utils.decorators import method_decorator
from django.db.models import Q

class PhotosQueryset(object):

    def get_photos_queryset(self, request):
        if not request.user.is_authenticated: # si no está utenticado
            photos = Photo.objects.filter(visibility=PUBLIC)
        elif request.user.is_superuser: # Si es administrador
            photos = Photo.objects.all()
        else: 
            photos = Photo.objects.filter(Q(owner=request.user) | Q(visibility=PUBLIC))
        return photos

class HomeView(View):

    def get(self, request):
        """
        Esta función devuelve el home de mi página
        """
        photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
        context = {
            'photos_list': photos[:5]
        }
        return render(request, 'photos/home.html', context)

class DetailView(View, PhotosQueryset):
    def get(self, request, pk):
        """
        Carga la página de detalle de una foto
        :param request: HttpRequest
        :param pk: id de la foto
        :return: HttpResponse
        """
        
        """ 
        También podemos utilizar esta sintaxis de recuperación de un objeto:
        try: 
            photo = Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            photo = None
        except Photo.MultipleObjectsReturned:
            photo = None """
        
        possible_photo = self.get_photos_queryset(request).filter(pk=pk).select_related('owner')
        photo = possible_photo[0] if len(possible_photo) == 1 else None
        if photo is not None:
            #Cargar plantilla de detalle
            context = {
                'photo': photo
            }
            return render(request, 'photos/detail.html', context)
        else:
            return HttpResponseNotFound('No existe la foto')


class CreateView(View):

    @method_decorator(login_required())
    def get(self, request):
        """
        Muestra un formulario para crear una foto
        :param request: HttpRequest
        :return: HttpResponse
        """
        form = PhotoForms()
        context = {
            'form': form,
            'success_message': ''
        }
        return render(request, 'photos/new_photo.html', context)
    
    @method_decorator(login_required())
    def post(self, request):
        """
        Crea una foto en vase a la información POST
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        photo_with_owner = Photo()
        photo_with_owner.owner = request.user # asigno como propietario de la foto, al usuario autenticado
        form = PhotoForms(request.POST, instance=photo_with_owner)
        if form.is_valid():
            new_photo = form.save() # Guarda el objeto y me lo devuelves
            form = PhotoForms()
            success_message = 'Guardado con éxito!'
            success_message += '<a href="{0}">'.format(reverse('photo_detail', args=[new_photo.pk]))
            success_message += "|Ver foto"
            success_message += '</a>'
        context = {
            'form': form,
            'success_message': success_message
        }
        return render(request, 'photos/new_photo.html', context)

class PhotoListView(View, PhotosQueryset):
    def get(self, request):
        """
        - Las fotos públicas si el usuario no está autenticado
        - Las fotos del usuario autenticado o las públicas de otros
        - Si el usuario es superadministrador, todas las fotos
        :param request: HttpRequest
        :return: HttpResponse
        """
        
        context = {
            'photos': self.get_photos_queryset(request)
        }
        return render(request, 'photos/photos_list.html', context)
    
class UserPhotosView(ListView):
    model = Photo
    template_name = 'photos/user_photos.html'

    def get_queryset(self):
        queryset = super(UserPhotosView, self).get_queryset()
        return queryset.filter(owner=self.request.user)
