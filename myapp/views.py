from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Person
from django.template import loader
from .forms import ItemForm

# Create your views here.
def index(request):
    person_list = Person.objects.all()
    context ={
        'person_list':person_list,
    }
    return render(request,'myapp/index.html',context)

def detail(request,person_id):
    item = Person.objects.get(pk = person_id)
    context ={
        'item':item,
    }
    return render(request,'myapp/detail.html',context)

def create_item (request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('myapp:index')

    return render(request,'myapp/item_form.html',{'form':form})

def delete_item(request,id):
    item = Person.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('myapp/index')
    return render(request,'myapp/item-delete.html',{item:'item'})
