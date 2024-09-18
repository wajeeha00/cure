from django.urls import path
from . import views

urlpatterns=[
    path('', views.MenuList.as_view(), name="home"),
    path('item/<int:pk>', views.MenuItemDetail.as_view(), name = "menu_item"),
    path('contact_us', views.contact_us, name = "contact_us")
]