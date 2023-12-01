from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied



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
    context['comment_form'] = CommentForm

    return render(
        request,
        'team/detail_content.html',
        context
    )

def base_detail_content(request):
    context=get_common_data()

    return render(
        request,
        'team/base_detail_content.html',
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
        context['comment_form']=CommentForm
        return context


# POST

def new_comment(request, pk):
    if request.user.is_authenticated:
        post = get_object_or_404(TeamMatchingPost, pk=pk)

        if request.method == 'POST':
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.teammatchingpost = post
                comment.author = request.user
                comment.save()
                return redirect(comment.get_absolute_url())
            else:
                return redirect(post.get_absolute_url())
        else:
            raise PermissionDenied

class PostCreate(CreateView, LoginRequiredMixin):
    model=TeamMatchingPost
    fields=['title', 'hook_text', 'content', 'main_category', 'sub_category']
    template_name = 'team/post_create_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user=self.request.user
        if current_user.is_authenticated:
            form.instance.author=current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/team/')

class PostUpdate(LoginRequiredMixin, UpdateView):
    model=TeamMatchingPost
    fields=['title', 'hook_text', 'content', 'main_category', 'sub_category']
    template_name = 'team/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class PostDelete(LoginRequiredMixin, DeleteView):
    model = TeamMatchingPost
    template_name = 'team/post_confirm_delete.html'
    success_url = '/team/'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied




# class TeamMatchingView(View):
#     template_name = 'team/team_matching.html'
#
#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get('pk')
#         context = {'pk': pk}
#         context.update(get_common_data())  # Update the context with common data
#         return render(request, self.template_name, context)

