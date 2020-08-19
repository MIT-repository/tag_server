from django.urls import path

from tag import views

urlpatterns = [
    path('<str:bucket>/<str:folder>/<str:name>/', views.tag, name="tag")
]
