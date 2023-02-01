from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    # Race URLS
    path('race_list/', views.race_list, name='race-list'),
    path('race_list/<int:race_id>', views.race_detail, name='race-detail'),
    # Character URLS
    path('character_list/', views.character_list, name='character-list'),
    path('character_list/<int:character_id>', views.character_detail, name='character-detail'),
    path('character_creator/', views.character_creation, name='char-create'),
    # Monster URLS
    path('monster_list/', views.monster_list, name='monster-list'),
    path('monster_list/search', views.monster_list_search, name='monster-list-search'),
    path('user_monster_list/', views.user_monster_list, name='user-monster-list'),
    path('user_monster_list/search', views.user_monster_list_search, name='user-monster-list-search'),
    path('monster_list/<int:monster_id>', views.monster_detail, name='monster-detail'),
]
