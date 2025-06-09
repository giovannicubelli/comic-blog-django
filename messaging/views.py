from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Max
from .models import Message
from .forms import MessageForm
from django.contrib import messages

@login_required
def message_list_view(request):
    user = request.user
    # Agrupar mensajes por conversación (con otro usuario)
    # Obtener el último mensaje de cada conversación
    conversations = Message.objects.filter(
        Q(sender=user) | Q(recipient=user)
    ).values('sender', 'recipient').annotate(
        latest_timestamp=Max('timestamp')
    ).order_by('-latest_timestamp')

    unique_conversations = []
    seen_users = set()

    for conv_data in conversations:
        other_user_id = conv_data['sender'] if conv_data['recipient'] == user.id else conv_data['recipient']
        if other_user_id not in seen_users:
            try:
                other_user = User.objects.get(pk=other_user_id)
                latest_message = Message.objects.filter(
                    (Q(sender=user, recipient=other_user) | Q(sender=other_user, recipient=user)),
                    timestamp=conv_data['latest_timestamp']
                ).first()

                if latest_message:
                    unique_conversations.append({
                        'other_user': other_user,
                        'latest_message': latest_message,
                    })
                    seen_users.add(other_user_id)
            except User.DoesNotExist:
                continue # Si el usuario fue borrado, saltar

    return render(request, 'messaging/message_list.html', {'messages_grouped': unique_conversations})


@login_required
def message_thread_view(request, username):
    other_user = get_object_or_404(User, username=username)
    user = request.user

    # Marcar mensajes como leídos al abrir el hilo
    Message.objects.filter(sender=other_user, recipient=user, is_read=False).update(is_read=True)

    thread_messages = Message.objects.filter(
        (Q(sender=user) & Q(recipient=other_user)) |
        (Q(sender=other_user) & Q(recipient=user))
    ).order_by('timestamp')

    if request.method == 'POST':
        # Formulario de respuesta simplificado, solo el cuerpo
        form = MessageForm(request.POST, initial={'recipient': other_user}) # Solo para validar el body
        if form.is_valid(): # Aquí solo validamos el body
            body = form.cleaned_data['body']
            Message.objects.create(sender=user, recipient=other_user, body=body)
            messages.success(request, "Mensaje enviado.")
            return redirect('message_thread', username=other_user.username)
        else:
            messages.error(request, "Hubo un error al enviar el mensaje.")
    else:
        # Formulario para enviar un nuevo mensaje en el hilo
        # No necesitamos el campo 'recipient' ni 'subject' visible aquí
        form = MessageForm(initial={'recipient': other_user})


    # Simplificamos el form para la respuesta, solo necesitamos el 'body'
    # Y el recipient ya lo tenemos por la URL
    reply_form_fields = MessageForm()
    reply_form_fields.fields.pop('recipient') # Quitamos para no mostrar en el template
    reply_form_fields.fields.pop('subject')   # Quitamos para no mostrar en el template


    return render(request, 'messaging/message_thread.html', {
        'other_user': other_user,
        'thread_messages': thread_messages,
        'form': reply_form_fields # Usamos el form simplificado
    })


@login_required
def message_create_view(request, recipient_username=None):
    initial_data = {}
    if recipient_username:
        try:
            recipient_user = User.objects.get(username=recipient_username)
            initial_data['recipient'] = recipient_user
        except User.DoesNotExist:
            messages.error(request, f"Usuario '{recipient_username}' no encontrado.")
            return redirect('message_list') # o a donde sea apropiado

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            messages.success(request, f"Mensaje enviado a {message.recipient.username}.")
            return redirect('message_thread', username=message.recipient.username)
    else:
        form = MessageForm(initial=initial_data)
        # No permitir que el usuario se envíe mensajes a sí mismo
        form.fields['recipient'].queryset = User.objects.exclude(pk=request.user.pk)

    return render(request, 'messaging/message_form.html', {'form': form})