from django.shortcuts import render
from .models import Contact
# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        c = Contact()
        c.name=name
        c.phone=phone
        c.email = email
        c.message = message
        c.save()
    return render(request,'contact.html')