from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Message
from django.db.models import Q
from django.contrib.auth.models import User


@login_required
def chat_view(request, user_id):
    current_user = request.user
    other_user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(
                sender=current_user,
                receiver=other_user,
                content=content
            )
            return redirect('chat', user_id=user_id)

    messages_list = Message.objects.filter(
        Q(sender=request.user, receiver=other_user) |
        Q(sender=other_user, receiver=request.user)
    ).order_by('timestamp')

    paginator = Paginator(messages_list, 10)
    page = request.GET.get('page')
    messages = paginator.get_page(page)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'chat/_messages.html', {'messages': messages})

    return render(request, 'chat/chat.html', {
        'other_user': other_user,
        'messages': messages
    })
