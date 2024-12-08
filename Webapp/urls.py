from django.urls import path
from Webapp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('our_products/', views.products, name="our_products"),
    path('category/', views.category, name="category"),
    path('savemsg/', views.savemsg, name="savemsg"),
    path('regsign/', views.regsign, name="regsign"),
    path('filterproducts/<cn>', views.filterproducts, name="filterproducts"),
    path('sproduct/<int:Id>', views.sproduct, name="sproduct"),
    path('signup/', views.registersignup, name="signup"),
    path('reglogin/', views.reglogin, name="reglogin"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('customer_logout/', views.customer_logout, name="customer_logout"),
    path('addCart/', views.addCart, name="addCart"),
    path('cartpage/', views.cartpage, name="cartpage"),
    path('checkoutpage/', views.checkoutpage, name="checkoutpage"),
    path('PaymentPage/', views.PaymentPage, name="PaymentPage"),
    path('BillAddress/', views.BillAddress, name="BillAddress"),
]
