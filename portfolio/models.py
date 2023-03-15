from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField



#Creamos una classe que va a heredar un modelo desde models
#esto nos sirve para poder emezar a denifirni que es lo que queremos guardar en el proyecto 

class Project(models.Model):
    title = CharField(max_length=100)
    description =CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
