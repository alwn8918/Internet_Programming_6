from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost

def get_subcategories(request):
    main_category_id = request.GET.get('main_category_id')
    subcategories = SubCategory.objects.filter(main_category_id=main_category_id)
    data = [{'id': subcategory.id, 'name': subcategory.name} for subcategory in subcategories]
    return JsonResponse(data, safe=False)


def get_common_data():
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    tags = Tag.objects.all()
    team_matching_posts = TeamMatchingPost.objects.all()

    return {
        'main_categories': main_categories,
        'sub_categories': sub_categories,
        'tags': tags,
        'team_matching_posts': team_matching_posts,
    }

def content(request):
    context=get_common_data()

    return render(
        request,
        'team/content.html',
        context
    )

def base_content(request):
    context=get_common_data()

    return render(
        request,
        'team/team_matching.html',
        context
    )

def detail_content(request, pk):
    context=get_common_data()
    context[pk]=pk

    return render(
        request,
        'team/detail_content.html',
        context
    )


class DetailContentView(DetailView):
    model = TeamMatchingPost
    template_name = 'team/detail_content.html'

    def get_context_data(self, **kwargs):
        context = super(DetailContentView, self).get_context_data(**kwargs)
        context.update(get_common_data())
        pk = self.kwargs['pk']
        context['pk'] = pk
        return context



def base_detail_content(request):
    context=get_common_data()

    return render(
        request,
        'team/base_detail_content.html',
        context
    )

# class TeamMatchingView(View):
#     template_name = 'team/team_matching.html'
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         context = {'pk': pk}
#         context.update(get_common_data())  # Update the context with common data
#         return render(request, self.template_name, context)

