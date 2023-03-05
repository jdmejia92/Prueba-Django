from django import forms
from django.core.exceptions import ValidationError
from photos.models import Photo
from photos.settings import BADWORDS

class PhotoForms(forms.ModelForm):
    """
    Formulario para el modelo photo
    """
    class Meta:
        model = Photo
        exclude = ['owner']

    def clean(self):
        """
        Valida si en la descripción se han puesto tacos definidos en settings.BADWORDS
        :return: diccionario con los atributos si OK
        """
        cleaned_data = super(PhotoForms, self). clean()

        description = cleaned_data.get('description', '')

        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise ValidationError('La palabra {0} no está permitida'.format(badword))
        # Si todo va OK devuelvo los datos limpios/normalizados
        return cleaned_data