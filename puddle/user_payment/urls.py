from django.urls import path
from . import views
app_name = 'user_payment'
urlpatterns = [
    path('',views.payment,name='payment'),
    path('success/',views.payment_successful,name='payment_successful'),
    path('cancel/',views.payment_cancelled,name='payment_cancelled'),

]