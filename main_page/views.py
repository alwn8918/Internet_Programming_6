from django.shortcuts import render
from django.views.generic import ListView
from guide.models import Guide
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

def index(request):
    return render(
        request,
        'main_page/mainpageTest.html',
    )

def calendar(request):
    return render(
        request,
        'main_page/index.html'
    )

class GuideList(ListView):
    model = Guide
    template_name = 'main_page/mainpageTest.html'
