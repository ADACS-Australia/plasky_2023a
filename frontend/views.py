from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from frontend.forms import SubjectForm
from frontend.models import Subject


def index(request):
    return render(request, 'index.html')


def add_subject(request):
    if request.method == "POST":
        subject = SubjectForm(request.POST)
        try:
            saved = subject.save()
        except ValueError:
            return render(
                request,
                'parts/add-subject-error.html',
                {'form': subject},
                status=400
            )

        return HttpResponse(
            headers={"HX-Redirect": reverse('view-subject', kwargs={'subject_id': saved.id})}
        )

    return render(request, 'add-subject.html')


def check_event_id(request):
    if Subject.objects.filter(event_id=request.POST['event_id']).exists():
        return HttpResponse("Event ID already exists")

    return HttpResponse("")


def view_subject(request, subject_id):
    return render(
        request,
        'view-subject.html',
        {'subject': Subject.objects.get(id=subject_id)}
    )
