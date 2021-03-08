from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def check_login(request):
    if request.user.is_authenticated:
        return redirect('chatview/')
    else:
        return redirect('account/login/')

def chatview(request):
    context = {'logged_in_name':request.user.username}
    return render(request,'Chatroom/index.html',context)

def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('../')
    return render(request, 'registration/sign_up.html', {'form': form})
