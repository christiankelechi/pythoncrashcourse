from django.shortcuts import render,redirect
from .forms import FruitPost
from .models import Fruit

# Create your views here.
def index(request):
    fruits=Fruit.objects.all()
    if request.method=="POST":
        fruitform=FruitPost(request.POST)
        if fruitform.is_valid():
            Fruit.objects.create(name=fruitform.cleaned_data['name'],color=fruitform.cleaned_data['color'],description=fruitform.cleaned_data['description'])
            context={'fruits':fruits}
            return redirect('firstapp:index')
    else:
        fruitform=FruitPost()
    context={'fruitform':fruitform,'fruits':fruits}
    return render(request,'index.html',context)