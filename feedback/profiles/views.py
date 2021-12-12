# step 1.3: In views.py, create class and assign the render template
# step 2.2: In views.py, temp create print statemnt to check the file upload is working or not, and add return HTTP responce 
# step 3.1: In views.py, create a function store_file using with statment as we are handling the file. - this will work only for jpg file.
# step 3.2: insted of printing the image name, use the function store_file, now create a temp folder and try upload a file now.
# step 4.2: In views.py, assign the created form in get function and post function, any how it wont help us to save the image
# step 5.4: In views.py, call the created model in post function as shown and save the image.
# step 7.1: In views.py. import from django.views.generic.edit import CreateView
# step 7.2: create new class using CreateView,  now you can remove all other class below, also no need of forms class, just model class is enough.
# step 8.2: In views.py, add new calss using generic ListView.



from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm    
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView


# Create your views here.

# def store_file(file):
#     with open("temp/image.jpg", "wb+") as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)

class CreateProfileView(CreateView):
    template_name = 'profiles/create_profile.html'
    model = UserProfile
    fields = '__all__'    
    success_url = '/profiles'
    
class ProfileList(ListView):
    template_name = 'profiles/profile_image.html'
    model = UserProfile
    context_object_name = "profiles"



# class CreateProfileView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(request, 'profiles/create_profile.html', {
#             'form' : form
#         } )

#     def post(self, request):
#         saved_form = ProfileForm(request.POST , request.FILES)

#         if saved_form.is_valid():
#             profile = UserProfile(image = request.FILES['user_image'] )
#             profile.save()
#             #store_file(request.FILES['image'])
#             return HttpResponseRedirect('/profiles')
        
#         return render(request, 'profiles/create_profile.html', {
#             'form' : saved_form
#         })

