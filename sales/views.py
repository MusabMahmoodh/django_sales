from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm

import pandas as pd
# Create your views here.
#function views are more readable than class views
def home_view(request):
    form  = SalesSearchForm(request.POST or None)
    
    if(request.method == "POST"):
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        qs = Sale.objects.filter(created__date=date_from)
        print('--------------')
        df1= pd.DataFrame(qs.values())
        
        print(df1)
        print('--------------')
        print('--------------')
        df2= pd.DataFrame(qs.values_list())
        
        print(df2)
        print('--------------')
    obj = Sale.objects.get(id=1)

    context = {
        'form': form
    }
    return render(request,'sales/home.html',context)

class SalesListView(ListView):
    #register view as a vew
    #can access object_list
    model = Sale
    template_name = 'sales/main.html'
    # by default object_list
    context_object_name = "qs"
    
# def sales_list_view(request):
#     qs = Sale.objects.all()
#     return render(request,'sales/main.html',{'object_lsit':qs})
    
class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    
# def sales_detail_view(request,**kwargs):
#      pk = kwargs.get('pk')
# 
# def sales_detail_view(request,pk):
#     qs = Sale.objects.get(pk=pk)
#     return render(request,'sales/detail.html',{'object':qs})

'''
In the urls:
path('sales/',sales_list_view, name="list")
path('sales/<pk>/',sales_detail_view, name="detail")
'''