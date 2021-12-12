# step 1.5: In main project urls.py file, import 'include' function, and add the path of created app urls.py file. 
# step 1.6: In main project urls.py include the path - "path("profiles/", include("profiles.urls"))"
# step 8.6: In main project urls.py, import and assign to urlparttens


"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('review.urls')),
    path('profiles/', include('profiles.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
