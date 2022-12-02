from django.shortcuts import render
from .models import Sellpost
# Create your views here.
def sellpost(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        pirce = request.POST.get('pirce')
        age= request.POST.get('age')
        description = request.POST.get('description')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        s=Sellpost()
        s.category = category
        s.pirce = pirce
        s.age = age
        s.description = description
        s.name = name
        s.contact = contact
        s.address =address
        s.save()
    return render(request,'post_sel.html')