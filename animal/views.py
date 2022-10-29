from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from animal.forms import AnimalForm
from animal.models import Animal, Animal

# Views

def listado(request):
	lista = serializers.serialize('json', Animal.objects.all().order_by('id'))
	return HttpResponse(lista, content_type='application/json')

def index(request):
    return render(request,'animal/index.html')

def animal_view(request):
    if request.method=='POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('animal_listar')
    else:
        form = AnimalForm()
    return render(request,'animal/animalForm.html',{'form':form})

def animal_list(request):
    animal = Animal.objects.all().order_by('id')
    contexto = {'animales':animal}
    return render(request,'animal/animalList.html',contexto)

def animal_edit(request,id_animal):
    animal = Animal.objects.get(id=id_animal)
    if request.method=='GET':
        form = AnimalForm(instance=animal)
    else:
        form = AnimalForm(request.POST,instance=animal)
        if form.is_valid():
            form.save()
        return redirect('animal_listar')
    return render(request,'animal/animalForm.html',{'form':form})

def animal_delete(request,id_animal):
    animal = Animal.objects.get(id=id_animal)
    if request.method=='POST':
        Animal.delete()
        return redirect('animal_listar')
    return render(request,'animal/animalDelete.html',{'animal':animal})

class AnimalList(ListView):
    model = Animal
    template_name = 'animal/animalList2.html'
    paginate_by = 5    
    ordering = ['id']

class AnimalCreate(CreateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animalForm.html'
    success_url = reverse_lazy('animal_listar2')

class AnimalUpdate(UpdateView):
    model = Animal
    form_class = AnimalForm
    template_name = 'animal/animalForm.html'
    success_url = reverse_lazy('animal_listar2')

class AnimalDelete(DeleteView):
    model = Animal
    template_name = 'animal/animalDelete2.html'
    success_url = reverse_lazy('animal_listar2')
