import razorpay
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from Backend.models import productdb, Category
from Webapp.models import servicedb, regdb, cartdb, billingDB


# Create your views here.


def homepage(req):
    cat = Category.objects.all()
    return render(req, "home.html", {'cat': cat})


def about(req):
    cat = Category.objects.all()
    return render(req, "about.html", {'cat': cat})


def contact(req):
    cat = Category.objects.all()
    return render(req, "contact.html", {'cat': cat})


def products(req):
    pro = productdb.objects.all()
    cat = Category.objects.all()
    return render(req, "ourproducts.html", {'pro': pro, 'cat': cat})


def category(req):
    cat = Category.objects.all()
    return render(req, "category.html", {'cat': cat})


def savemsg(req):
    if req.method == "POST":
        na = req.POST.get('name')
        em = req.POST.get('email')
        su = req.POST.get('subject')
        me = req.POST.get('message')
        ph = req.POST.get('phone')
        obj = servicedb(name=na, email=em, subject=su, message=me, phone=ph)
        obj.save()
        return redirect(contact)


def filterproducts(req, cn):
    data = productdb.objects.filter(cname=cn)
    cat = Category.objects.filter(cname=cn)
    return render(req, "ProductsFiltered.html", {'data': data, 'cat': cat})


def sproduct(req, Id):
    data = productdb.objects.filter(id=Id)
    cat = Category.objects.all()
    return render(req, "singleproduct.html", {'data': data, 'cat': cat})


def regsign(req):
    return render(req, "customersignin.html")


def customerlogin(req):
    return render(req, "customerlogin.html")


def registersignup(req):
    if req.method == "POST":
        uname = req.POST.get('uname')
        email = req.POST.get('email')
        password = req.POST.get('password1')
        img = req.FILES['p_img']
        obj = regdb(uname=uname, email=email, password=password, p_img=img)
        if regdb.objects.filter(uname=uname).exists():
            messages.warning(req, "User already exists..!")
        elif regdb.objects.filter(email=email).exists():
            messages.warning(req, "User already exists..!")
        else:
            obj.save()
        return redirect(regsign)


def reglogin(req):
    if req.method == "POST":
        un = req.POST.get('uname')
        pw = req.POST.get('password')
        if regdb.objects.filter(uname=un, password=pw).exists():
            customer = regdb.objects.get(uname=un, password=pw)
            req.session['username'] = un
            req.session['password'] = pw
            req.session['email'] = customer.email
            req.session['img'] = customer.p_img.url
            messages.success(req, "login successfull")
            return redirect('homepage')
        else:
            messages.warning(req, "invalid Username or Password")
            return redirect('customerlogin')
    else:
        messages.warning(req, "User not found..!")
        return redirect('customerlogin')


def customer_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(homepage)


def addCart(req):
    if req.method == "POST":
        uname = req.POST.get('uname')
        pname = req.POST.get('pname')
        quantity = req.POST.get('quantity')
        total = req.POST.get('total')
        obj = cartdb(uname=uname, pname=pname, quantity=quantity, total=total)
        obj.save()
        messages.success(req, "Added to Cart")
        return redirect(homepage)


def cartpage(req):
    data = cartdb.objects.filter(uname=req.session['username'])
    cat = Category.objects.all()
    total_price = 0
    for i in data:
        total_price = total_price + i.total
    cost = 0
    if total_price > 500:
        cost = 0
    else:
        cost = 100
    total = cost + total_price
    return render(req, "cart.html",
                  {'data': data, 'total_price': total_price, 'cost': cost, 'total': total, 'cat': cat})


def checkoutpage(req):
    data = cartdb.objects.filter(uname=req.session['username'])
    cat = Category.objects.all()
    total_price = 0
    for i in data:
        total_price = total_price + i.total
    cost = 0
    if total_price > 500:
        cost = 50
    elif total_price >= 1000:
        cost = 0
    else:
        cost = 100
    total = cost + total_price
    return render(req, "checkout.html",
                  {'data': data, 'total_price': total_price, 'cost': cost, 'total': total, 'cat': cat})


def PaymentPage(req):
    # retrieve the bilingdb data by specified id
    customer = billingDB.objects.order_by('-id').first()
    # get the amount of the specified customer
    payy = customer.Total
    # convert the amount into paisa (the smallest currency unit)
    amount = int(payy * 100)
    # convert the amount into string for printing
    payy_str = str(amount)
    # printing the character of the amount
    for i in payy_str:
        print(i)
    if req.method == "POST":
        order_currency = "INR"
        client = razorpay.Client(auth=('rzp_test_NDm0Gc1tG1rdOG', 'BuPpRCm9e8mIQuAPozFAvxJl'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})
    return render(req, "payment.html", {'customer': customer, 'payy_str': payy_str})


def BillAddress(req):
    if req.method == "POST":
        uname = req.POST.get('uname')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        place = req.POST.get('place')
        total = req.POST.get('total')
        address = req.POST.get('address')
        message = req.POST.get('message')
        obj = billingDB(uname=uname, email=email, phone=phone, address=address, message=message, place=place,
                        Total=total)
        obj.save()
        messages.success(req, "directing to payment")
        return redirect(PaymentPage)
