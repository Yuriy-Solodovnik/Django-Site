from django.db.models import Q
from django.shortcuts import render

from .models import Message


def index(request):
    return render(request, 'main/index.html')


def messages(request):
    search_query = request.GET.get('search', '')
    if search_query:
        message = Message.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query)).reverse()
    else:
        message = Message.objects.order_by('date').reverse()
    return render(request, 'main/messages.html', {'title': 'Сообщения', 'messages': message})
