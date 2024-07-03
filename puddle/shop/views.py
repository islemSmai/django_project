from django.shortcuts import render , get_object_or_404,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Shop,AboutUs
from item.models import Item,Category
from .formShop import NewShopForm,EditShopForm
from .form import NewAboutUsForm,EditAboutUsForm

@login_required
def newShop(request):
    if request.method == 'POST':
        form = NewShopForm(request.POST,request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.created_by = request.user
            shop.save()
            return redirect('shop:detail',pk=shop.id)
    else:
        form = NewShopForm()
    return render(request,'shop/form.html',{
        'form': form,
        'title': 'New shop',
    })
@login_required
def editShop(request,pk):
    shop = get_object_or_404(Shop,created_by=request.user,pk=pk)
    if request.method == 'POST':
        form = EditShopForm(request.POST,request.FILES,instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop:detail',pk=shop.id)
    else:
        form = EditShopForm(instance=shop)
    return render(request,'shop/form.html',{
        'form': form,
        'title': 'Edit shop',
    })
def detailShop(request,pk):
    shop = get_object_or_404(Shop,pk=pk)
    categories = Category.objects.filter(shop=shop)[:3] 
    about_us = AboutUs.objects.filter(shop=shop)
    related_items = Item.objects.filter(category__in=categories,is_sold=False)[:8]
    return render(request, 'shop/detail.html',{
        'shop':shop,
        'categories':categories,
        'related_items':related_items,
        'about_us':about_us
    })
def shops(request):
    query = request.GET.get('query','')
    shops =Shop.objects.all()
    if query:
        shops = shops.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'shop/shops.html',{
        'shops':shops,
        'query':query,
    })
@login_required
def deleteShop(request,pk):
    shop = get_object_or_404(Shop,pk=pk,created_by=request.user)
    shop.delete()
    return redirect('shop/shops.html')
@login_required
def about_us(request):
    if request.method == 'POST':
        form = NewAboutUsForm(request.POST,request.FILES)
        if form.is_valid():
            about_us = form.save(commit=False)
            about_us.shop = get_object_or_404(Shop,created_by=request.user)
            about_us.save()
            return redirect('shop:detail',pk=about_us.shop.id)
    else:
        form = NewAboutUsForm()
    return render(request,'about_us/form.html',{
        'form': form,
        'title': 'About-us',
    })
def about_us_shop(request,pk):
    shop = get_object_or_404(Shop,pk=pk)
    about_us = AboutUs.objects.filter(shop=shop)
    return render(request, 'about_us/about_us_shop.html',{
        'shop':shop,
        'about_us':about_us
    })