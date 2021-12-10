from django.urls import path
# step 1.4: create urls.py file and create urlparttens and assign path.

from .import views

urlpatterns = [
    path("", views.CreateProfileView.as_view())
]