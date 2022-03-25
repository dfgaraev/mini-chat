from django.urls import path

from chat.views import msg, add_msg

urlpatterns = [
    path('msg/', msg),
    path('send-msg/', add_msg),
]
