from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, ),
    path( 'delete/<int:post_id>/', views.delete, name='delete' ),


]
