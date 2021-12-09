# step 1.4: In urls.py, import path, views and create the urlpatterns.
# step 5.6: include PATH in urls.py and call the thankyou function.
# step 16.2: in urls.py, add .as_view().



from django.urls import path
from .import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path('thankyou', views.thankyou )
]
