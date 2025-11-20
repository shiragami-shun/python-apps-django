from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="chat"),
    path("start/", views.start_conversation, name="start_conversation"),
    path("conversations/", views.conversation_list, name="conversation_list"),
    path("conversation/<int:conversation_id>/", views.conversation_detail, name="conversation_detail"),
]
