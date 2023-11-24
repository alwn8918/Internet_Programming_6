from django import forms
from .models import TeamMatchingPost, SubCategory

class TeamMatchingPostForm(forms.ModelForm):
    class Meta:
        model = TeamMatchingPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(TeamMatchingPostForm, self).__init__(*args, **kwargs)
        if 'main_category' in self.fields:
            self.fields['main_category'].widget.attrs['onchange'] = 'update_subcategories()'
        if 'sub_category' in self.fields:
            self.fields['sub_category'].queryset = SubCategory.objects.none()
