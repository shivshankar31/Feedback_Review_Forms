# step 1.4: In urls.py, import path, views and create the urlpatterns.

from django.urls import path
from .import views 

urlpatterns = [
    path("", views.review )
]
