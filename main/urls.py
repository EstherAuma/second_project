from django.urls import path
from . import views
from django.contrib.auth import views as auth_views







urlpatterns = [
    # path('',views.base, name='base'),
    path('home/',views.home, name='home'),
    path('create_branch/',views.create_branch, name='create_branch'),
    path('create_country/',views.create_country, name='create_country'),
    path('create_category/',views.create_category, name='create_category'),
    path('create_product/',views.create_product, name='create_product'),
    path('create_sale/',views.create_sale, name='create_sale'),

    
    path('login/',auth_views.LoginView.as_view(template_name ='spare/login.html'), name = 'login'),
    path('register/',views.register, name='register'),

    

     
]

