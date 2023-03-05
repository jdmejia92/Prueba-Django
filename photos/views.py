from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from photos.models import Photo, PUBLIC

# Create your views here.

def home(request):
    """
    Esta función devuelve el home de mi página
    """
    photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
    context = {
        'photos_list': photos[:5]
    }
    return render(request, 'photos/home.html', context)

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
