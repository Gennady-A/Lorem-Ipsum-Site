from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.


def main(request):
    return render(request, 'main\index.html')

def lorem_ipsum(request):
    return render(request, 'main\lorem_ipsum.html')

def rusLI(request):
    if request.method == 'POST':
        url = 'http://www.lipsum.com/feed/xml'
        data = request.POST
        print(data)
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

        ans = ''

        url = f'https://www.lipsum.com/feed/xml?amount={amount}&what={what}&start={start}'
        print(url)
        req = requests.get(url)
        page = BeautifulSoup(req.text, "lxml")
        ans = (page.find('lipsum')).text
        print(ans)

        return render(request, 'main\RusTemp.html', {'generatorText': ans})
    return render(request, 'main\RusTemp.html')

def engLI(request):
    return render(request, 'main\EngTemp.html')

def danLI(request):
    return render(request, 'main\DanTemp.html')

def deuLI(request):
    return render(request, 'main\DeuTemp.html')