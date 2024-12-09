from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar_avance, name='registrar_avance'),
    path('ajax/load-alas/', views.load_alas, name='load_alas'),
    path('ajax/load-puntos/', views.load_puntos, name='load_puntos'),
    path('success/', views.success, name='success'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registro/', views.registrar_avance, name='registrar_avance'),
]
