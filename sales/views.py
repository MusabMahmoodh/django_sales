from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
# Create your views here.
#function views are more readable than class views
def home_view(request):
    return render(request,'sales/home.html',{})

class SalesListView(ListView):
    #register view as a vew
    #can access object_list
    model = Sale
    template_name = 'sales/main.html'
    # by default object_list
    context_object_name = "qs"
    
class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'