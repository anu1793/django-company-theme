from django.shortcuts import render

# Create your views here.
def index(request):
    values = {'text': "Anusha", 'age':25}
    return render(request, "basic_app/index.html",values)

def others(request):
    return render(request, "basic_app/others.html")

def relative(request):
    return render(request, "basic_app/relative.html")

def base(request):
    return render(request, "basic_app/base.html")
