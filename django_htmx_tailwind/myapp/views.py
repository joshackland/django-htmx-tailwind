from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'myapp/index.html')

def load_data(request):
    data = {'message': 'This is dynamic data from the server.'}
    return render(request, 'myapp/data_template.html', data)
