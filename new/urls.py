from django.urls import path
from . import views

urlpatterns = [
    # new/views-homeメソッドにつなぐ
    path('', views.home, name='home'),
    # add/views-addTodoメソッドにつなぐ
    path('add', views.addTodo, name='add')

]