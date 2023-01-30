from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('race_list/', views.race_list, name='race-list'),
    path('race_list/<int:race_id>', views.race_detail, name='race-detail'),
    path('character_list/', views.character_list, name='character-list'),
    path('character_list/<int:character_id>', views.character_detail, name='character-detail'),
    path('character_creator/', views.character_creation, name='char-create'),
    path('monster_list/', views.monster_list, name='monster-list'),
]