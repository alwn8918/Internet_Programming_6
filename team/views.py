from django.shortcuts import render
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost

def content(request):
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    tags=Tag.objects.all()
    team_matching_posts=TeamMatchingPost.objects.all()

    return render(
        request,
        'team/content.html',
        {
            'main_categories': main_categories,
            'sub_categories': sub_categories,
            'tags': tags,
            'team_matching_posts': team_matching_posts,
        }
    )

def team_matching(request):
    main_categories = MainCategory.objects.all()
    sub_categories = SubCategory.objects.all()
    tags=Tag.objects.all()
    team_matching_posts=TeamMatchingPost.objects.all()

    return render(
        request,
        'team/team_matching.html',
        {
            'main_categories': main_categories,
            'sub_categories': sub_categories,
            'tags': tags,
            'team_matching_posts': team_matching_posts,
        }
    )