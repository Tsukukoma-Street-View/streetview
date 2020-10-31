from django.urls import path

from . import views

app_name = 'streetview'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('view/', views.scene_view, name='view'),
    path('view/ajax/', views.ajax_transition, name='ajax_transition'),
]