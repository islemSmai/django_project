import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404,redirect
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime
from django.db.models.functions import TruncMonth
from item.models import Item,Category
from shop.models import Shop
from user_payment.models import Payment
stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def index(request):
    shop = Shop.objects.filter(created_by=request.user).first()
    items=""
    cathegory=""
    sold_out_items=0
    payments=0
    months=0
    totals=0
    if shop:
        cathegory=Category.objects.filter(shop=shop)
        items =Item.objects.filter(is_sold=False,category__in=cathegory)
        payments = Payment.objects.filter(product__in=items)
        sold_out_items =Item.objects.filter(is_sold=True,category__in=cathegory)
        payments_per_month = (Payment.objects
                          .filter(product__in=items)
                          .annotate(month=TruncMonth('purchaseDate'))
                          .values('month')
                          .annotate(total_amount=Sum('amount'))
                          .order_by('month'))
        months = [payment['month'].strftime('%Y-%m') for payment in payments_per_month]
        totals = [payment['total_amount'] for payment in payments_per_month]
    return render(request,'dashboard/index.html',{
        'items':items,
        "sold_out_item":sold_out_items,
        'categories':cathegory,
        'payments':payments,
        "shop":shop,
        'months': months,
        'totals': totals,
        "shop_exists":shop
    })
@login_required
def payment(request):
    YOUR_DOMAIN="item/detail.html"
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    return JsonResponse({
        'id':checkout_session.id
    })

