from django.contrib import admin
from .models import MainCategory, SubCategory, Tag, TeamMatchingPost
from django import forms


class MainCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(MainCategory, MainCategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)

class TeamMatchingPostAdminForm(forms.ModelForm):
    class Meta:
        model = TeamMatchingPost
        fields = '__all__'

class TeamMatchingPostAdmin(admin.ModelAdmin):
    form = TeamMatchingPostAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "main_category" and "main_category" in request.GET:
            main_category_id = request.GET["main_category"]
            kwargs["queryset"] = db_field.related_model.objects.filter(main_category_id=main_category_id)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(TeamMatchingPost, TeamMatchingPostAdmin)