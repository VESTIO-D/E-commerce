from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import Category, productdb
from Webapp.models import servicedb


# Create your views here.


def indexpage(req):
    return render(req, "index.html")


def contactDet(req):
    data = servicedb.objects.all()
    return render(req, "ContactDetails.html", {'data': data})


def Add_cat(req):
    return render(req, "add.html")


def saveCategory(req):
    if req.method == "POST":
        cname = req.POST.get('cname')
        description = req.POST.get('description')
        img = req.FILES['category_image']
        obj = Category(cname=cname, description=description, c_img=img)
        obj.save()
        messages.success(req, 'Saved Successful!')
        return redirect(Add_cat)


def cdetails(req):
    data = Category.objects.all()
    return render(req, "category_details.html", {'data': data})


def edit(req, Id):
    data = Category.objects.get(id=Id)
    return render(req, "updatecategory.html", {'data': data})


def updatec(req, Id):
    if req.method == "POST":
        na = req.POST.get('cname')
        de = req.POST.get('description')
        try:
            img = req.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = Category.objects.get(id=Id).c_img
        Category.objects.filter(id=Id).update(cname=na, description=de, c_img=file)
        messages.warning(req, "updated successfully")
        return redirect(cdetails)


def delc(req, Id):
    data = Category.objects.filter(id=Id)
    data.delete()
    messages.error(req, "deleted...!")
    return redirect(cdetails)


def product_page(req):
    cat = Category.objects.all()
    return render(req, "addproducts.html", {'cat': cat})


def productsave(req):
    if req.method == "POST":
        cname = req.POST.get('cname')
        pname = req.POST.get('pname')
        description = req.POST.get('description')
        price = req.POST.get('price')
        img = req.FILES['product_image']
        obj = productdb(cname=cname, pname=pname, description=description, price=price, c_img=img)
        obj.save()
        messages.success(req, 'Saved Successful!')
        return redirect(product_page)


def pdetails(req):
    data = productdb.objects.all()
    return render(req, "product_details.html", {'data': data})


def pedit(req, p_id):
    pro = productdb.objects.get(id=p_id)
    cat = Category.objects.all()
    return render(req, "product_edit.html", {'pro': pro, 'cat': cat})


def updatep(req, p_id):
    if req.method == "POST":
        pname = req.POST.get('pname')
        cname = req.POST.get('cname')
        description = req.POST.get('description')
        price = req.POST.get('price')
        try:
            img = req.FILES['product_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=p_id).c_img
        productdb.objects.filter(id=p_id).update(cname=cname, pname=pname, description=description, price=price, c_img
        =file)
        messages.warning(req, "updated successfully")
    return redirect(pdetails)


def delp(req, p_id):
    data = productdb.objects.filter(id=p_id)
    data.delete()
    messages.error(req, "deleted...!")
    return redirect(pdetails)


def loginpage(req):
    return render(req, "login.html")


def adminlog(req):
    if req.method == "POST":
        na = req.POST.get('username')
        psw = req.POST.get('password')
        if User.objects.filter(username__contains=na).exists():
            x = authenticate(username=na, password=psw)
            if x is not None:
                login(req, x)
                req.session['username'] = na
                req.session['password'] = psw
                messages.success(req, "login successfull")
                return redirect('indexpage')
            else:
                messages.warning(req, "invalid Username or Password")
                return redirect('login')
        else:
            messages.warning(req, "User not found..!")
            return redirect('login')


def delContact(req, Id):
    data = servicedb.objects.filter(id=Id)
    data.delete()
    return redirect(contactDet)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginpage)
