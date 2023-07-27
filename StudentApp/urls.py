from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.login_fun,name='log'),
    path('regdata',views.reg_fun,name='reg'),
    path('insert',views.insert_fun,name='insert'),
    path('display',views.display_fun,name='display'),
    path('update/<int:id>',views.update_fun,name='update'),
    path('del/<int:id>',views.delete_fun,name='del'),
    path('home',views.home_fun,name='home'),
    path('log_out',views.logout_fun,name='log_out')
]