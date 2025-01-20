from django.shortcuts import render
from .models import Launch, Rocket, Payload

# Create your views here.
def index(request):
      return render(request, "spaceXlaunchTracker/index.html")

def about(request):
      return render(request, "spaceXlaunchTracker/about.html")

#Launches information
def launches(request):
    launch_url = "https://api.spacexdata.com/v5/launches/latest"
    launches = request.get(launch_url).json()
    return render(request, "spaceXlaunchTracker/launches.html", {
        "launches": launches
    })