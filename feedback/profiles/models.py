# step 5.1: create model with models.filefield(upload_to = "image") image is a folder name where saves the image we upload.



from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.FileField(upload_to="image")