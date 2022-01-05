
from django.shortcuts import render, redirect
from django.views import generic

from django.views.generic import ListView
from .models import Follower
class IndexView(generic.TemplateView):
    template_name = 'index.html'
    def post(self, request):
            email = request.POST.get('email')
            f = Follower.objects.filter(email=email)
            if f:
            
                return redirect ("index")
            if email:
                f = Follower(email=email)
                f.save()
               
            return redirect('index')

class ShopView(generic.TemplateView):
    template_name = 'shop.html'

class AboutView(generic.TemplateView):
    template_name = 'about.html'

class ContactView(generic.TemplateView):
    template_name = 'contact.html'

           