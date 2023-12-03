from django.shortcuts import render
from django.views.generic import ListView
from .models import Guide, Category, TagType, TagTeam
from django.db.models import Q

def guide(request):
    guides = Guide.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        'guide/guide.html',
        {
            'guides':guides,
            'categories':categories,
        }
    )

def category_page(request, slug):
    category = Category.objects.get(slug=slug)

    return render (
        request,
        'guide/guide.html',
        {
            'guide_list': Guide.objects.filter(category=category),
            'categories': Category.objects.all(),
            'category': category,
        }
    )

def tagtype_page(request, slug):
    tagtype = TagType.objects.get(slug=slug)

    return render (
        request,
        'guide/guide.html',
        {
            'guide_list': Guide.objects.filter(tagtype=tagtype),
            'tagtype': tagtype,
            'tagtypes':TagType.objects.all(),
        }
    )

def tagteam_page(request, slug):
    tagteam = TagTeam.objects.get(slug=slug)

    return render (
        request,
        'guide/guide.html',
        {
            'guide_list': Guide.objects.filter(tagteam=tagteam),
            'tagteam': tagteam,
            'tagteams':TagTeam.objects.all(),
        }
    )

class GuideList(ListView):
    model = Guide
    template_name = 'guide/guide.html'

    def get_context_data(self, **kwargs):
        context = super(GuideList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['tagtypes'] = TagType.objects.all()
        context['tagteams'] = TagTeam.objects.all()
        return context

class GuideSearch(GuideList):
    def get_queryset(self):
        q = self.kwargs['q']
        guide_list = Guide.objects.filter(
            Q(title__contains=q)
        ).distinct()
        return guide_list

    def get_context_data(self, **kwargs):
        context = super(GuideSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context