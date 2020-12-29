from django.shortcuts import render, HttpResponse


def home(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse("About")