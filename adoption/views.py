from django.shortcuts import render
from adoption_post.models import AdoptionPost
# Create your views here.
def adoption(request):
    adop = AdoptionPost.objects.all()
    data = {'Sellpost':adop}
    return render(request,'adoption.html',data)