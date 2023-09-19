from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('del_emp/<int:id>', views.del_emp, name='del_emp'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('update_emp/<int:id>', views.update_emp, name='update_emp'),
]