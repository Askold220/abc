from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.user.is_authenticated: 
        return render(request, 'accounts/already_logged_in.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return render(request, 'accounts/login.html', {'error': 'Неправильный email или пароль'})
    else:
        return render(request, 'accounts/login.html')
