from django.shortcuts import render,redirect
from django.http import HttpResponse
from panel.models import Members 
from panel.models import Orders
from panel.forms import OrdersForm
from django.contrib import messages
from django.contrib.sessions.models import Session

# Create your views here.

def dashboard(request):
    return render(request,'dashboard/index.html')

def register(request):
    if request.method =='POST':
        Name=request.POST['name']
        Email=request.POST['email']
        Mobile=request.POST['mobile']
        Pwd=request.POST['pwd']
        Members(name=Name,email=Email,pwd=Pwd,mobile=Mobile).save()
        messages.success(request,"Saved Successfully..!")
        return render(request,'panel/register.html')
    else:
          return render(request,'panel/register.html')

def login(request):
    if request.method =='POST':
        try:
            Userdetails=Members.objects.get(email=request.POST['email'],pwd=request.POST['pwd'])
            request.session['email']
            return render(request,'index.html')
        except Members.DoesNotExist as e:
            messages.success(request,'Email/ Password Invalid..!')
    return render(request,'panel/login.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')


def orders(request):
    query_results = Orders.objects.all()
    return render(request, 'dashboard/orders_tables.html', {'objs':query_results})

def ordersform(request):
    if request.method == "POST":
        form = OrdersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/orders_tables')
            except:
                pass

    form=OrdersForm()
    return render(request,'dashboard/ordersform.html',{'form': form})


def ordersedit(request,id):
    user = Orders.objects.get(id=id)
    return render(request, 'dashboard/orders_edit.html', {'objs':user})

def ordersupdate(request,id):
    user= Orders.objects.get(id=id)
    form=OrdersForm(request.POST,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/orders_tables')
    return render(request,'dashboard/orders_edit.html', {'objs':user})

def ordersdelete(request,id):
    item=Orders.objects.get(id=id)
    item.delete()
    return redirect('/orders_tables')


def banners(request):
    return render(request,'dashboard/banners_tables.html')