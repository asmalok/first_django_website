# from django.shortcuts import render

# # Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Type

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ClothView(generic.DetailView):
    model = Type
    template_name = 'cloth.html'
    
    # def get(self, request):
    #     print(self)
    #     return HttpResponse(self.type)

    # def redirect_to_specified_clothing(request):
    #     return HttpResponseRedirect(reverse('pants', args=(pants)))