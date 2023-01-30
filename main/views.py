from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'main\index.html')

def lorem_ipsum(request):
    return render(request, 'main\lorem_ipsum.html')

def rusLI(request):
    return render(request, 'main\RusTemp.html')

def engLI(request):
    return render(request, 'main\EngTemp.html')

def danLI(request):
    return render(request, 'main\DanTemp.html')

def deuLI(request):
    return render(request, 'main\DeuTemp.html')