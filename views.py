from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from . form import message_gen_form
from django.http import HttpResponse
import datetime
from . models import Users, Messages

def user_reg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Users.objects.create(user=user)
            return redirect('message')
        else:
            return redirect('user_reg')
    else:
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})

def message(request):
    message = Messages.objects.all()
    return render(request, 'message/chatroom.html', {'chat':message})

def gen_message(request):
    if request.method == 'POST':
        form = message_gen_form(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            user, created = Users.objects.get_or_create(user=request.user)  
            msg.sender = user    
            msg.created_at = datetime.datetime.now()
            msg.save()
            return HttpResponse('thank you')
        else:
            return redirect('message')
        
    else:
        form = message_gen_form()
        return render(request, 'message/create_msg.html', {'form': form})
    
    
    
            