from django.urls import path
from . import views
app_name = 'item'
urlpatterns = [
    path('',views.items,name='items'),
    path('new/',views.new,name='new'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit'),
    path('category',views.cathegory,name='cathegory'),
    path('newCathegory',views.newCathegory,name='newCathegory'),
    path('<int:pk>/editCategory/',views.editCategory,name='editCategory'),
    path('<int:pk>/deleteCathegory',views.deleteCathegory,name='deleteCathegory'),
]