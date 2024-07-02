from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('',views.shops,name='shops'),
    path('new/',views.newShop,name='new'),
    path('<int:pk>/edit/',views.editShop,name='edit'),
    path('<int:pk>/detail/',views.detailShop,name='detail'),
    path('<int:pk>/delete/',views.deleteShop,name='delete'),
    path('about-us/',views.about_us,name='about_us'),
    path('<int:pk>/about-us-shop/',views.about_us_shop,name='about_us_shop'),
]