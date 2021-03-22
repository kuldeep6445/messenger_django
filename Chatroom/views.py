from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.models import User

def check_login(request):
    if request.user.is_authenticated:
        return redirect('chatview/')
    else:
        return redirect('account/login/')

def chatview(request):
    t = request.POST.get('xyz','')
    l = []
    for x in User.objects.filter(username__contains='t'):
        l.append(x.username)
        print(x.username)
    print(l)
    context = {'logged_in_name':request.user.username,'items':l}
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
