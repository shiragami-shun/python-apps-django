from django.shortcuts import render, redirect, get_object_or_404
from .models import Conversation, Message
from .ai_client import ask_ai


def index(request):
    return render(request, "chat/index.html")


def start_conversation(request):
    conv = Conversation.objects.create(title="New Conversation")
    return redirect("conversation_detail", conversation_id=conv.id)


def conversation_detail(request, conversation_id):
    conv = get_object_or_404(Conversation, id=conversation_id)
    if request.method == "POST":
        user_message = request.POST.get("message")
        # 1) User message 保存
        Message.objects.create(
            conversation=conv,
            role="user",
            content=user_message
        )
        # 2) AIに送信
        ai_response = ask_ai(user_message)

        # 3) AI message 保存
        Message.objects.create(
            conversation=conv,
            role="assistant",
            content=ai_response
        )
        return redirect("conversation_detail", conversation_id=conv.id)

    return render(request, "chat/conversation_detail.html", {
        "conversation": conv,
        "messages": conv.messages.all(),
    })


def conversation_list(request):
    conversations = Conversation.objects.order_by("-created_at")
    return render(
        request, "chat/conversation_list.html", {
            "conversations": conversations
            }
        )
