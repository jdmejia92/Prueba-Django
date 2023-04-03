from django.db import models
from photos.validators import badwords_detector
from django.contrib.auth.models import User
from photos.settings import LICENSES

PUBLIC = 'PUB'
PRIVATE = 'PRI'

VISIBILITY = (
    (PUBLIC, 'Publica'),
    (PRIVATE, 'Privada')
)

class Photo(models.Model):

    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, default="", validators=[badwords_detector])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    license = models.CharField(max_length=3, choices=LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __str__(self): # 0 param method / before was __unicode__
        return self.name