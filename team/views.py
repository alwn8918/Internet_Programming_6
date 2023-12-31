from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
import traceback  # Import the traceback module
import logging
import json
from django.core.serializers import serialize
from django.template.loader import render_to_string
from django.template.response import TemplateResponse



# Configure logging (add this at the beginning of your file)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_main_category_posts(request, slug):
    main_category = MainCategory.objects.get(slug=slug)
    main_category_posts = TeamMatchingPost.objects.filter(main_category=main_category)

    context = {
        'isCategorized': True,
        'team_matching_posts': main_category_posts,
        'main_category': main_category
    }


    return render(
        request,
        'team/content.html',
        context
    )

def get_sub_category_posts(request, slug_main, slug_sub):
    main_category = MainCategory.objects.get(slug=slug_main)
    sub_category = SubCategory.objects.get(main_category=main_category, slug=slug_sub)
    # 같은 코드
    # sub_category = SubCategory.objects.filter(main_category__slug=slug_main, slug=slug_sub)

    sub_category_posts = TeamMatchingPost.objects.filter(sub_category=sub_category)


    context = {
        'isCategorized': True,
        'team_matching_posts': sub_category_posts,
        'main_category': main_category,
        'sub_category': sub_category
    }

    return render(
        request,
        'team/content.html',
        context
    )


def get_common_data():
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    tags = Tag.objects.all()
    team_matching_posts = TeamMatchingPost.objects.all().order_by('-pk')

    return {
        'main_categories': main_categories,
        'sub_categories': sub_categories,
        'tags': tags,
        'team_matching_posts': team_matching_posts,
    }


def filtered_content(request):
    context = get_common_data()

    try:
        if request.method == 'POST':
            # Log the request body
            logger.debug('Request Body: %s', request.body.decode('utf-8'))

            # Load JSON data from the request body
            data = json.loads(request.body.decode('utf-8'))
            logger.debug('Received Data: %s', data)

            selected_subcategories = data.get('sub_categories', [])

            # Convert the IDs to integers
            selected_subcategories = [int(sub_category_id) for sub_category_id in selected_subcategories]
            #
            # Filter TeamMatchingPost instances based on selected subcategories
            matching_posts = TeamMatchingPost.objects.filter(sub_category__id__in=selected_subcategories)
            # matching_posts = list(matching_posts.values())

            context['matching_posts'] = matching_posts

            # 해당되는 포스트가 0개일 경우 {{% if matching_posts %}}가 먹히지 않으므로 flag를 만듦
            context['isFiltered']=True

            # Render the template with the filtered data
            html_content = render(request, 'team/content_template.html', context).content.decode('utf-8')

            # Return the HTML content in the JSON response
            return JsonResponse({'html_content': html_content})

        return render(request, 'team/content_template.html', context)

    except Exception as e:
        # Log the exception for debugging
        logger.error('Error in team_view: %s', str(e), exc_info=True)
        return JsonResponse({'error': str(e)})


def content(request):
    context = get_common_data()

    return render(
        request,
        'team/content.html',
        context
    )


def base_content(request):
    context = get_common_data()

    return render(
        request,
        'team/detail_content.html',
        context
    )


def detail_content(request, pk):
    context = get_common_data()
    context[pk] = pk
    context['comment_form'] = CommentForm

    return render(
        request,
        'team/detail_content.html',
        context
    )


def base_detail_content(request):
    context = get_common_data()

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
        context['comment_form'] = CommentForm
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
    model = TeamMatchingPost
    fields = ['title', 'hook_text', 'content', 'main_category', 'sub_category']
    template_name = 'team/post_create_form.html'

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/team/')


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = TeamMatchingPost
    fields = ['title', 'hook_text', 'content', 'main_category', 'sub_category']
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
