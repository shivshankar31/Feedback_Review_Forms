# step 1.4: In urls.py, import path, views and create the urlpatterns.
# step 5.6: include PATH in urls.py and call the thankyou function.
# step 16.2: in urls.py, add .as_view().
# step 19.4: add new path in urls.py
# step 20.3: In urls.py, assign the path, also generate the extension using <int:id>.
# step 21.3: In urls.py, convert <int:id> to <int:pk>



from django.urls import path
from .import views 

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path('thankyou', views.ThankyouView.as_view()),
    path('reviewlist', views.ReviewList.as_view()),
    path('reviewlist/<int:pk>',views.ReviewDetailview.as_view())# for methed 2 replace <int:id> to <pk>
]
