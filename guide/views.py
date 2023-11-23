from django.shortcuts import render
from .models import Guide, Category

def guide(request):
    guides = Guide.objects.all()

    return render(
        request,
        'guide/guide.html',
        {
            'guides':guides,
        }
    )