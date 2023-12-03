from django.contrib import admin
from .models import Guide, Category, TagType, TagTeam

admin.site.register(Guide)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TagTeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(TagType, TagTypeAdmin)
admin.site.register(TagTeam, TagTeamAdmin)



