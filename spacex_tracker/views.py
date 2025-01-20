from django.shortcuts import render
from .models import Launch, Rocket, Payload
# Create your views here.
def index(request):
      return render(request, "spaceXlaunchTracker/index.html")

def about(request):
      return render(request, "spaceXlaunchTracker/about.html")
