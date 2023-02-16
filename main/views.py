from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def getLorem(data):
    if ('amount' in data):
        amount = data['amount']
    else:
        amount = 10

    if ('what' in data):
        what = data['what']
    else:
        what = 'words'

    if ('start' in data):
        start = 'yes'
    else:
        start = 'no'

    url = f'https://www.lipsum.com/feed/xml?amount={amount}&what={what}&start={start}'

    req = requests.get(url)
    page = BeautifulSoup(req.text, "lxml")
    ans = (page.find('lipsum')).text

    return ans


def main(request):
    return render(request, 'main\index.html')

def lorem_ipsum(request):
    return render(request, 'main\lorem_ipsum.html')

def rusLI(request):
    if request.method == 'POST':
        data = request.POST
        ans = getLorem(data)
        return render(request, 'main\RusTemp.html', {'generatorText': ans})
    return render(request, 'main\RusTemp.html')

def engLI(request):
    if request.method == 'POST':
        data = request.POST
        ans = getLorem(data)
        return render(request, 'main\EngTemp.html', {'generatorText': ans})
    return render(request, 'main\EngTemp.html')

def danLI(request):
    if request.method == 'POST':
        data = request.POST
        ans = getLorem(data)
        return render(request, 'main\DanTemp.html', {'generatorText': ans})
    return render(request, 'main\DanTemp.html')

def deuLI(request):
    if request.method == 'POST':
        data = request.POST
        ans = getLorem(data)
        return render(request, 'main\DeuTemp.html', {'generatorText': ans})
    return render(request, 'main\DeuTemp.html')