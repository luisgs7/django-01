from django.shortcuts import render

def python(request):
    return render(request, 'sobre/app.html')
