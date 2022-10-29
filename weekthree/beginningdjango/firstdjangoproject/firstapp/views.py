from django.shortcuts import render,redirect
from .forms import FruitPost
from .models import Fruit

# Create your views here.
def index(request):
    fruits=Fruit.objects.all()
    if request.method=="POST":
        fruitform=FruitPost(request.POST)
        if fruitform.is_valid():
            Fruit.objects.create(name=request.POST['name'],color=request.POST['color'],description=request.POST['description'])
            context={'fruits':fruits}
            return redirect('firstapp:index')
    else:
        fruitform=FruitPost()
    context={'fruitform':fruitform,'fruits':fruits}
    return render(request,'index.html',context)