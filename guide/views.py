from django.shortcuts import render
from .models import Guide

def guide(request):
    guides = Guide.objects.all()

    return render(
        request,
        'guide/guide.html',
        {
            'guides':guides,
        }
    )
