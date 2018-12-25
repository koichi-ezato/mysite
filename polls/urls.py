from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.QuestionCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.QuestionUpdateView.as_view(), name='update'),
]
