from django.contrib import admin
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost

admin.site.register(TeamMatchingPost)

class MainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MainCategory, MainCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
