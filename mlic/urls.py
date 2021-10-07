from django.urls import path
from . import views

app_name = 'mlic'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('submit/', views.submit, name='submit'),
    path('result/<int:result_id>', views.result, name='result'),
    path('feedback/', views.feedback, name='feedback'),
]