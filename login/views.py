import json
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.models import User
#from .models import Users

#안 쓰는 듯?...

class LoginView(View):
    def login(self, request):
        data = json.loads(request.body)
        User(
            username = data['username'],
            password = data['password'],
        )

        if User.objects.filter(username = data['username']).exists():
            user = User.objects.get(username = data['username'])
            if user.password == data['password']:
                return JsonResponse({"message":"로그인에 성공하셨습니다."}, status = 200)
            else:
                return JsonResponse({"message" : "비밀번호가 일치하지 않습니다."}, status = 200)
        return JsonResponse({'message':'학번 또는 사번을 찾을 수 없습니다.'}, status=200)
        
    def get(self, request):
        user = User.objects.values()
        return JsonResponse({"list":list(user)}, status = 200)