from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_subject(request):
    return render(request, 'add-subject.html')
