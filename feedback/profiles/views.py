# step 1.3: In views.py, create class and assign the render template
# step 2.2: In views.py, temp create print statemnt to check the file upload is working or not, and add return HTTP responce 

from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        return render(request, 'profiles/create_profile.html' )

    def post(self, request):
        print(request.FILES['image'])
        return HttpResponseRedirect('/profiles')