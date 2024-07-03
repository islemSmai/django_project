from django.shortcuts import render , get_object_or_404,redirect
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import Item,Category,Image
from .forms import NewItemForm,EditItemForm
from shop.models import Shop
from .formCategory import NewCategoryForm,EditCategoryForm
from django.contrib.auth.models import User
from django.db.models import F, Window
from django.db.models.functions import RowNumber
def items(request):
    query = request.GET.get('query','')
    category_name = request.GET.get('category','')
    shop_id = request.GET.get('shop',0)
    shop = ''
    if shop_id:
        categories = Category.objects.filter(Q(shop_id=shop_id) & Q(items__isnull=False)).distinct()
        shop = get_object_or_404(Shop,id=shop_id)
        items =Item.objects.filter(is_sold=False,category__in=categories)
        if category_name:
            categories_item=categories.filter(name=category_name)
            items = items.filter(category__in=categories_item)
        if query:
            items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    else:
        #categories = Category.objects.filter(items__isnull=False).distinct()
        categories = Category.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[F('name')],
                order_by=F('id').asc())).filter(row_number=1)
        items =Item.objects.filter(is_sold=False)
        if category_name:
            categories_item = Category.objects.filter(name=category_name)
            items = items.filter(category__in=categories_item)
        if query:
            items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_nam':category_name, 
        'shop':shop,
    })
def detail(request,pk):
    item = get_object_or_404(Item,pk=pk)
    images = Image.objects.filter(item=item)
    related_items = Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)[0:5]
    return render(request, 'item/detail.html',{
        'item':item,
        'images':images,
        'related_items':related_items,
    })
@login_required
def new(request):
    shop = get_object_or_404(Shop, created_by=request.user)
    if request.method == 'POST':
        form = NewItemForm(request.POST,request.FILES,shop=shop)
        if form.is_valid():
            item = form.save(commit=False)
            uploaded_files = request.FILES.getlist('gallery')
            item.save()
            for file in uploaded_files:
                Image.objects.create(item=item, gallery=file)
            return redirect('item:detail',pk=item.id)
    else:
        form = NewItemForm(shop=shop)
    return render(request,'item/form.html',{
        'form': form,
        'title': 'New item',
    })
@login_required
def edit(request,pk):
    item = get_object_or_404(Item,pk=pk)
    if request.method == 'POST':
        form = EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request,'item/form.html',{
        'form': form,
        'title': 'Edit item',
    })
@login_required
def delete(request,pk):
    item = get_object_or_404(Item,pk=pk)
    item.delete()
    return redirect('item:items')
#Categories
def cathegory(request):
    shop_id = request.GET.get('shop',0)
    if shop_id:
        categories = Category.objects.filter(Q(shop_id=shop_id) & Q(items__isnull=False)).distinct()
        shop = get_object_or_404(Shop,id=shop_id)
    else:
        categories = Category.objects.filter( Q(items__isnull=False))
        shop = ''
    
    return render(request,'cathegory/cathegories.html',{
        'categories':categories,
        'shop':shop,
    })
@login_required
def newCathegory(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST,request.FILES)
        if form.is_valid():
            cathegory = form.save(commit=False)
            cathegory.shop = get_object_or_404(Shop,created_by=request.user)
            cathegory.save()
            return redirect('item:cathegory')
    else:
        form = NewCategoryForm()
    return render(request,'cathegory/cathegories.html',{
        'form': form,
        'title': 'New cathegory',
        'is_edit': False,
    })
@login_required
def editCategory(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = EditCategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect('item:cathegory')
    else:
        form = EditCategoryForm(instance=category)
    return render(request,'cathegory/cathegories.html',{
        'form': form,
        'title': 'Edit category',
        'category':category,
        'is_edit': True,
    })
@login_required
def deleteCathegory(request,pk):
    cathegory = get_object_or_404(Category,pk=pk)
    cathegory.delete()
    return redirect('item:cathegory')