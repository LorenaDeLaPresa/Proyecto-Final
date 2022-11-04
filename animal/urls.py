from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.animal.views import index, animal_view, animal_list, animal_edit, animal_delete, AnimalList, AnimalCreate, AnimalUpdate, AnimalDelete, listado

urlpatterns = [
    path('', login_required(index), name='index'),
    path('nuevo/', login_required(animal_view), name='animal_crear'),
    path('nuevo2/', login_required(AnimalCreate.as_view()), name='animal_crear2'),
    path('listar/', login_required(animal_list), name='animal_listar'),
    path('listar2', login_required(AnimalList.as_view()), name='animal_listar2'),
    path('editar/<id_animal>/', login_required(animal_edit), name='animal_editar'),
    path('editar2/<pk>/', login_required(AnimalUpdate.as_view()), name='animal_editar2'),
    path('eliminar/<id_animal>/', login_required(animal_delete), name='animal_eliminar'),
    path('eliminar2/<pk>/', login_required(AnimalDelete.as_view()), name='animal_eliminar2'),
    path('listado/', login_required(listado), name='listado'),
]