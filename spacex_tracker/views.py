from django.shortcuts import render

# Create your views here.
def index(request):
      return render(request, "spacex_tracker/index.html")