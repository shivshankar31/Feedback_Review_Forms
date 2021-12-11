# step 5.1: create model with models.filefield(upload_to = "image") image is a folder name where saves the image we upload.
# step 6.1: In models.py change Filefield to ImageField



from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="image") #FileField will allow all type of files, but imagefiels will allow only image.