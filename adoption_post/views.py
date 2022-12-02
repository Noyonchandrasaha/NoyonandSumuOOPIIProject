from django.shortcuts import render
from .models import AdoptionPost
# Create your views here.
def adoptionpost(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        age= request.POST.get('age')
        description = request.POST.get('description')
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        address = request.POST.get('address')
        a=AdoptionPost()
        a.category = category
        a.age = age
        a.description = description
        a.name = name
        a.contact = contact
        a.address =address
        a.save()
    return render(request,'adoption_post.html')