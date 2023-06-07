from django.urls import path
from . import views


urlpatterns = [
    path('chat/', views.Newchat.as_view(), name="chat"),
    path('chatmessage/', views.Newchat.as_view(), name="chat_message"),
]
