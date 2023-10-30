from django.conf import settings

from frontend.models import Subject


def global_context(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
        'project_name': settings.ASIMOV_PROJECT
    }
    return context
