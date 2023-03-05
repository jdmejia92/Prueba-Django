from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC
from photos.forms import PhotoForms
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home(request):
    """
    Esta función devuelve el home de mi página
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

@login_required()
def detail(request, pk):
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
    
    possible_photo = Photo.objects.filter(pk=pk)
    photo = possible_photo[0] if len(possible_photo) == 1 else None
    if photo is not None:
        #Cargar plantilla de detalle
        context = {
            'photo': photo
        }
        return render(request, 'photos/detail.html', context)
    else:
        return HttpResponseNotFound('No existe la foto')

@login_required()
def create(request):
    """
    Muestra un formulario para crear una foto y la crea si la petición es POST
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PhotoForms()
    else:
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
