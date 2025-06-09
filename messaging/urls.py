from django.urls import path
from .views import message_list_view, message_thread_view, message_create_view

urlpatterns = [
    path('', message_list_view, name='message_list'),
    path('new/', message_create_view, name='message_create'),
    path('new/<str:recipient_username>/', message_create_view, name='message_create_to'), # Para iniciar mensaje a alguien específico
    path('thread/<str:username>/', message_thread_view, name='message_thread'),
]