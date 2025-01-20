from django.shortcuts import render, get_object_or_404
from .models import Launch, Rocket, Payload
import requests
# Create your views here.
def index(request):
      return render(request, "spaceXlaunchTracker/index.html")

def about(request):
      return render(request, "spaceXlaunchTracker/about.html")

#Launches information
def launches(request):
    launch_url = "https://api.spacexdata.com/v4/launches"
    launches = requests.get(launch_url).json()
    return render(request, "spaceXlaunchTracker/launches.html", {
        "launches": launches
    })

def launch_detail(request, launch_id):
    # Fetch launch details
    launch_url = f"https://api.spacexdata.com/v4/launches/{launch_id}"
    launch_response = requests.get(launch_url)
    
    if launch_response.status_code != 200:
        return render(request, "spaceXlaunchTracker/error.html", {"message": "Launch not found"})
    
    launch = launch_response.json()
    
    # Extract rocket and payload IDs from launch data
    rocket_id = launch.get("rocket")
    payload_ids = launch.get("payloads", [])
    
    # Fetch rocket details
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_response = requests.get(rocket_url)
    
    if rocket_response.status_code != 200:
        return render(request, "spaceXlaunchTracker/error.html", {"message": "Rocket not found"})
    
    rocket = rocket_response.json()
    
    # Fetch payload details
    payloads = []
    for payload_id in payload_ids:
        payload_url = f"https://api.spacexdata.com/v4/payloads/{payload_id}"
        payload_response = requests.get(payload_url)
        
        if payload_response.status_code == 200:
            payloads.append(payload_response.json())
    
    return render(request, "spaceXlaunchTracker/launch_detail.html", {
        "launch": launch,
        "rocket": rocket,
        "payloads": payloads
    })