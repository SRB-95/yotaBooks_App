app_name = 'myapp'
from .import views
from django.urls import path

urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:person_id>/',views.detail,name='detail'),
    path('add',views.create_item,name="create_item"),
    path('delete/<int:id>/',views.delete_item,name= 'delete_item'),
]