from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='quiz-index'),
    path('search/', views.search_view, name='quiz-search'),
    path('learn/<str:document_id>/', views.learn_view, name='quiz-learn'),
]