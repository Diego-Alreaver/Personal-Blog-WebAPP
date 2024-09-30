from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
