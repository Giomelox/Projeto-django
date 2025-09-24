from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),  # index principal
    path('tecnologia/', views.produtos_tecnologia, name='produtos_tecnologia'),
    path('vestuario/', views.produtos_vestuario, name='produtos_vestuario'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
]
