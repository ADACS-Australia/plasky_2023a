from django.conf import settings

from frontend.models import Subject


def global_context(request):
    subjects = Subject.objects.all().order_by('event_id')
    context = {
        'subjects': subjects,
        'project_name': settings.ASIMOV_PROJECT
    }
    return context
