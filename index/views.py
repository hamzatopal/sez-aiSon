from django.shortcuts import render
from .models import Index
# Create your views here.
def index(request):
    indexs=Index.objects.all()    
    return render(request,"index.html",{"indexs":indexs})