from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('providers/', views.provider_list, name='provider_list'),
    path('provider/<int:provider_id>/', views.provider_detail, name='provider_detail'),
    path('book/<int:provider_id>/', views.book_appointment, name='book_appointment'),
]
