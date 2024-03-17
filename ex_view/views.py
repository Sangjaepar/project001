from django.http import HttpResponse
from django.shortcuts import render

from django.utils import timezone

# Create your views here.

def index(request):
    now = timezone.now()
    print('현재시간:', now)
   
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
