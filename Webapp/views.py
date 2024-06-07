from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from Backend.models import productdb, Category
from Webapp.models import servicedb, regdb, cartdb


# Create your views here.


def homepage(req):
    cat = Category.objects.all()
    return render(req, "home.html", {'cat': cat})


def about(req):
    return render(req, "about.html")


def contact(req):
    return render(req, "contact.html")


def products(req):
    pro = productdb.objects.all()
    return render(req, "ourproducts.html", {'pro': pro})


def category(req):
    cat = productdb.objects.all()
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
    return render(req, "singleproduct.html", {'data': data})


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
    total_price = 0
    for i in data:
        total_price = total_price + i.total
    pow = total_price/200
    shipping=400
    cost=shipping-pow*10
    return render(req, "cart.html", {'data': data, 'total_price': total_price, 'cost':cost})
