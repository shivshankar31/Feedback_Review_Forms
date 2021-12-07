# step 1.4: In urls.py, import path, views and create the urlpatterns.
# step 5.6: include PATH in urls.py and call the thankyou function.




from django.urls import path
from .import views 

urlpatterns = [
    path("", views.review ),
    path('thankyou', views.thankyou )
]
