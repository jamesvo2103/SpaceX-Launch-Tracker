from django.shortcuts import render
from .models import Launch, Rocket, Payload
import requests
# Create your views here.
def index(request):
      return render(request, "spaceXlaunchTracker/index.html")

def about(request):
      return render(request, "spaceXlaunchTracker/about.html")

#Launches information
def launches(request):
    launch_url = "https://api.spacexdata.com/v5/launches"
    launches = requests.get(launch_url).json()
    return render(request, "spaceXlaunchTracker/launches.html", {
        "launches": launches
    })

def launch_detail(request, launch_id):
    launch_url = f"https://api.spacexdata.com/v5/launches/{launch_id}"
    launch = requests.get(launch_url).json()
    return render(request, "spaceXlaunchTracker/launch_detail.html", {
        "launch": launch
    })