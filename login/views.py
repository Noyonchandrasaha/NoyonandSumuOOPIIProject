from django.shortcuts import render
from .models import Register
# Create your views here.
def login(request):
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw = request.POST.get('pass')
        re_pass= request.POST.get('re_pass')
        r = Register()
        r.name = name
        r.email = email
        r.passw = passw
        r.re_pass = re_pass
        r.save()
    return render(request,'register.html')