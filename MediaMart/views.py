from django.shortcuts import render, HttpResponse

def home(request):
    print('request recived')
    return render(request, 'index.html')