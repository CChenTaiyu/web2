"""pay2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pay_xyf.views import register, login, deposit, payment_check,\
    statement, transfer_user, balance_list, payment_detail, payment_return, payment_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Payment_weha/signup/', register),
    path('Payment_weha/signin/', login),
    path('Payment_weha/deposit/', deposit),
    path('Payment_weha/Payment_check/', payment_check),
    path('Payment_weha/statement/', statement),
    path('Payment_weha/transfer/', transfer_user),
    path('Payment_weha/balance/', balance_list),
    path('Payment_weha/Payment_information/', payment_detail),
    path('Payment_weha/Payment_return/', payment_return),
    path('Payment_weha/Payment_order/', payment_order)
]
