from django.shortcuts import render, redirect, get_object_or_404
from item.models import Category,Item
from shop.models import Shop
from .forms import SignupForm
from .contact import ContactForm
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render


def index(request):
    shops = Shop.objects.all()[0:6]
    categories = Category.objects.all()[:6]
    return render(request,'core/index.html',{
        'categories':categories,
        'shops':shops,
    })
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'contact'
            message = form.message
            email_from = form.useremail
            recipient_list = [settings.EMAIL_HOST_USER, ]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('core/contact.html')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', 
                  {'form': form})
def about_us_is(request):
    return render(request,'core/about_us.html')
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print("work")
        if form.is_valid():
            form.save()
            return redirect('/login/')  # Redirect to the login URL
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', 
                  {'form': form})
def myShop(request):
    shop = get_object_or_404(Shop,created_by=request.user)
    categories = Category.objects.filter(shop=shop)[0:6]
    related_items = Item.objects.filter(category__in=categories,is_sold=False)[:8]
    return render(request, 'shop/detail.html',{
        'shop':shop,
        'categories':categories,
        'related_items':related_items,
    })