from frontend.models import Subject


def global_context(request):
    subjects = Subject.objects.all()
    context = {'subjects': subjects,}
    return context
