from django.shortcuts import render , get_object_or_404,redirect
from django.db.models import Q
import stripe
import time
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import BadHeaderError, send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import stripe.error
from .models import Payment
from item.models import Item

@login_required
def payment(request):
    YOUR_DOMAIN="http://127.0.0.1:8000"
    stripe.api_key=settings.STRIPE_SECRET_KEY
    if request.method =='POST':
        pk = request.GET.get('id',0)
        item = get_object_or_404(Item,pk=pk)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                        },
                        'unit_amount': int((item.price*100)/3.12),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=f'{YOUR_DOMAIN}/payment/success/?session_id={{CHECKOUT_SESSION_ID}}&id={item.id}',
            cancel_url=f'{YOUR_DOMAIN}/payment/cancel/',
        )
        return redirect(checkout_session.url, code=303)
    return render(request,'item/detail')
def payment_successful(request):
    session_id = request.GET.get('session_id', None)
    pk = request.GET.get('id', 0)
    item = get_object_or_404(Item,pk=pk)
    item.quantity = item.quantity-1
    if item.quantity == 0:
        item.is_sold = True
    item.save()
    shop = item.category.shop
    shop.profit = shop.profit + item.price
    shop.save()
    if session_id is None:
        return HttpResponse("Error: session_id is missing", status=400)
    
    try:
        session = stripe.checkout.Session.retrieve(session_id)
        subject = "Order "+item.name+" confirmed"
        pay = Payment(
            email=session.customer_details.email,
            product=item,
            payment_bool=True,
            stripe_checkout_id=session_id,
            amount=(session.amount_total / 100)*3.12  # Convert cents to dollars if applicable
        )
        pay.save()
        
        return render(request, 'success.html', {'session': session})
        
    except stripe.error.InvalidRequestError as e:
        print(f"Stripe error: {e}")
        return HttpResponse(f"Error retrieving session: {e}", status=400)
def payment_cancelled(request):
    return render(request,'user_payment/cancel.html')
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key=settings.STRIPE_SECRET_KEY
    time.sleep(10)
    payload = request.body
    signature_header = request.MERA['HTTP_STRIPE_SIGNATURE']
    event =None
    try:
        event= stripe.Webhook.construct_event(
            payload,signature_header,settings.STRIPE_SECRET_KEY
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id=session.get('id',None)
        time.sleep(15)
        return HttpResponse(status=200)

