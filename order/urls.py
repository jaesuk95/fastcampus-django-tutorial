from django.urls import path
from order import views

urlpatterns = [
    path('shops/', views.shop, name='shop'),
    path('menu/', views.menu, name='all_menu'),
    # int:shop, shop 아이디를 찾아 부른다
    path('menu/<int:shop>', views.menu_from_shop, name='get_menu'),
    path('order/', views.order, name='order')
]
