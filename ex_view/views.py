from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.utils import timezone
from django.urls import reverse

# Create your views here.

def index(request):
    now = timezone.now()
    print('현재시간:', now)
    print(reverse('exview:index'))
    print(reverse('exview:get1'))
    print(reverse('exview:get2', args=(11, 22, 'hello')))
    return render(request, 'ex_view/index.html', {'now': now})

def get1(request):
    print('get1/ 요청이 들어왔다')
    keys = request.GET.keys()
    for key in keys:
        value = request.GET[key]
        print(f'{key}:{value}')
    return HttpResponse('get1')

def get2(request, n1, n2, n3):
    print('n1:', n1)
    print('n2:', n2)
    print('n3:', n3)
    return HttpResponse('get2')

def post1(request):
    print('post1/ 요청이 들어왔다')
    keys = request.POST.keys()
    print(int(request.POST['n1']) + int(request.POST['n2']))
    for key in keys:
        value = request.POST[key]
        print(f'{key}:{value}')

    return HttpResponse('post1')

def post2(request, msg, n):
    print('post2/ 요청이 들어왔다')
    print('msg: ', msg)
    print('n: ', n)
    keys = request.POST.keys()
    print(int(request.POST['n1']) + int(request.POST['n2']))
    for key in keys:
        value = request.POST[key]
        print(f'{key}:{value}')

    return HttpResponse('post2')

def getpost1(request):
    print(request.method)
    if request.method == 'GET':
        print("GET요청에 대한 처리")
    elif request.method == 'POST':
        print("POST요청에 대한 처리")
    return HttpResponse('getpost1')

# 클래스형 뷰
from django.views.generic import View

class ExamGet3(View):
    def get(self, request):
        print('get3/ 요청이 들어왔다')
        keys = request.GET.keys()
        print(int(request.GET['n1']) + int(request.GET['n2']))
        for key in keys:
            value = request.GET[key]
            print(f'{key}:{value}')
        return HttpResponse('get3')
    
class ExamGet4(View):
    def get(slef, request, n1, n2, n3):
        print('n1:', n1)
        print('n2:', n2)
        print('n3:', n3)
        return HttpResponse('get4')
    
class ExamPost3(View):
    def post(self, request):
        print('post3/ 요청이 들어왔다')
        keys = request.POST.keys()
        print(int(request.POST['n1']) + int(request.POST['n2']))
        for key in keys:
            value = request.POST[key]
            print(f'{key}:{value}')
        return HttpResponse('post3')
    
class ExamPost4(View):
    def post(slef, request, msg, n):
        print('post4/요청이 들어옴')
        print('msg: ', msg)
        print('n: ', n)
        keys = request.POST.keys()
        print(int(request.POST['n1']) + int(request.POST['n2']))
        for key in keys:
            value = request.POST[key]
            print(f'{key}:{value}')
        return HttpResponse('post4')
    

class ExamGetPost(View):
    def get(self, request):
        print('GET요청 동작')
        return HttpResponse('getpost2/(GET)')

    def post(self, request):
        print('POST요청 동작')
        user = request.POST['user']
        pwd = request.POST['pwd']
        if user == pwd:
            print('로그인 성공')
            return HttpResponse('getpost2/(POST)')
        else:
            print('로그인 실패(다시 폼 전송)')
            return HttpResponseRedirect(reverse('exview:index'))        
        
