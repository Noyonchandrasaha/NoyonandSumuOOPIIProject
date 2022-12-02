from django.shortcuts import render
from sell_post.models import Sellpost
# Create your views here.
def shop(request):
    shoppets = Sellpost.objects.all()
    data = {'Sellpost':shoppets}
    return render(request,'shop.html',data)