from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('character_list/', views.character_list, name='character-list'),
    path('character_list/<int:character_id>', views.character_detail, name='character-detail'),
    path('character_creator/', views.character_creation, name='char-create'),
    path('monster_list/', views.monster_list, name='monster-list'),
]