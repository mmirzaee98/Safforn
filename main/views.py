from django.shortcuts import render
from main.models import ContactMessage

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        ContactMessage.objects.create(
            name=name,
            email=email,
            text=text,
        )
        message = "Your message is submited"
    else:
        message = None

    return render(request, 'contact.html', {'message':message})

def faq(request):
    return render(request, 'faq.html')

def home(request):
    return render(request, 'home.html')

def terms(request):
    return render(request, 'terms.html')
    