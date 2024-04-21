from django.http import HttpResponse
from django.shortcuts import render

# информация о запросе

def index(request):
    context = {
        'title'
    }

    return render(request,'main/index.html' )
def about(request):
    return HttpResponse('About page')