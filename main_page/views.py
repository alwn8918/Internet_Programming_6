from django.shortcuts import render

# Create your views here.

def main(request):
    return render(
        request,
        'main_page/main.html' #(임시)main html 생기면 고쳐 줘야
    )