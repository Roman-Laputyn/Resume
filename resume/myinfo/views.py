from django.shortcuts import render


def index(request):
    return render(request, 'myinfo/index.html', {'title': 'Resume'})
