from django import forms
#from .models import Users
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

#사실상 안 씀
# User = get_user_model

class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')

    username = forms.CharField(max_length=20, label="학번 또는 사번",
        error_messages={
            'required': '학번을 입력해주세요'
        })
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호",
        error_messages={
            'required': '비밀번호를 입력해주세요'
        })
    
    def clean(self):                                           
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password :
            try:
                user = User.objects.get(username=username)
                if not check_password(password, user.password):
                    self.add_error('password', '비밀번호가 일치하지 않습니다.')
                else:
                    self.user_id = user.id
            #except Exception
            except User.DoesNotExist:
                self.add_error('username', '존재하지 않는 학번입니다.')