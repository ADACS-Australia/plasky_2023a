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
        if subject.is_valid():
            saved = subject.save()
            return HttpResponse(
                headers={"HX-Redirect": reverse('view-subject', kwargs={'subject_id': saved.id})}
            )

        return render(
            request,
            'parts/add-subject-form.html',
            {'form': subject}
        )

    subject = SubjectForm()
    return render(request, 'add-subject.html', {'form': subject})


def view_subject(request, subject_id):
    return render(
        request,
        'view-subject.html',
        {'subject': Subject.objects.get(id=subject_id)}
    )
