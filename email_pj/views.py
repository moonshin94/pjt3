from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("안녕하세요 email_pj 사이트 입니다")
# Create your views here.
