from django.urls import path
from .views import home
from .views import loginuser
from .views import createtodo
from .views import logoutuser
from.views import currenttodos
from .views import signupuser
from .views import viewtodo
from .views import completedtodos
from .views import deletetodo
from .views import completetodo

urlpatterns = [
    path('', home, name='home'),
    path('create/', createtodo, name='createtodo'),
    path('signup/', signupuser, name='signupuser'),
    path('current/', currenttodos, name='currenttodos'),
    path('completed/', completedtodos, name='completedtodos'),
    path('logout/', logoutuser, name='logoutuser'),
    path('login/', loginuser, name='loginuser'),
    path('todo/<int:todo_pk>', viewtodo, name='viewtodo'),
    path('todo/<int:todo_pk>/complete', completetodo, name='completetodo'),
path('todo/<int:todo_pk>/delete', deletetodo, name='deletetodo'),
]