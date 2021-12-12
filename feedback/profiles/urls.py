from django.urls import path
# step 1.4: create urls.py file and create urlparttens and assign path.
# step 8.3: In urls.py, add the path for created view class.



from .import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("list", views.ProfileList.as_view())
]