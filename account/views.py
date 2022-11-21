from django.shortcuts import render

# Create your views here.

def signup_view(request):
    return render(request, 'account/signup.html')



def login_view(request):
    if request.method == 'POST':
        print(request.method)
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, '-------', password)

    return render(request, 'account/login.html')