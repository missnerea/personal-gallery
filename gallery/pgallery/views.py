from django.shortcuts import render
from .models import image
import datetime as dt
# Create your views here.
 def index (request):
     title = 'Welcome to the gallery'
     date = dt.date.today()
     
     return render (request,'index.html')