from django.shortcuts import render

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def receipt(request):
    return render(request, 'receipt.html')

def my_account(request):
    return render(request, 'my_account.html')
