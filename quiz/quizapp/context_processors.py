from .models import Category
def cat(request):
    c=Category.objects.all()
    return {'clink':c}