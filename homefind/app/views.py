from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from twitter_data_receiving.main import mainReceiver


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return render(request,"login.html")

def search(request):

    return render(request,"search.html")

def name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        zip = request.POST.get('zip', None)
        radius = request.POST.get('radius', None)
        tweets, users = mainReceiver(zip, radius)
        # for i in range(5):
        #     print("%s : %s" % (users[i], tweets[i]))
        # check whether it's valid:
        # process the data in form.cleaned_data as required
        # ...
        # redirect to a new URL:
        return render(request, 'name.html', {'zip': zip, 'radius': radius})


    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponse(status=400)

# Create your views here.
