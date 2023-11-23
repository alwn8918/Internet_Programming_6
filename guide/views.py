from django.shortcuts import render
from django.views.generic import ListView
from .models import Guide, Category

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

class GuideList(ListView):
    model = Guide
    template_name = 'guide/guide.html'

    def get_context_data(self, **kwargs):
        context = super(GuideList, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context
