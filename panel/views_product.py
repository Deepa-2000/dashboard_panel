from django.shortcuts import render
from panel.models import Products
# from panel.forms import ProductsForm



def products(request):
    query_results = Products.objects.all()
    return render(request, 'dashboard/products_tables.html', {'objs':query_results})

# def productsform(request):
#      if request.method == "POST":
#          form = ProductsForm(request.POST)
#          if form.is_valid():
#              try:
#                  form.save()
#                  return redirect('/products_tables')
#              except:
#                  pass
#      form=ProductsForm()
#      return render(request,'dashboard/productsform.html',{'form': form})


# def ordersedit(request,id):
#     user = Orders.objects.get(id=id)
#     return render(request, 'dashboard/orders_edit.html', {'objs':user})

# def ordersupdate(request,id):
#     user= Orders.objects.get(id=id)
#     form=OrdersForm(request.POST,instance=user)
#     if form.is_valid():
#         form.save()
#         return redirect('/orders_tables')
#     return render(request,'dashboard/orders_edit.html', {'objs':user})

# def ordersdelete(request,id):
#     item=Orders.objects.get(id=id)
#     item.delete()
#     return redirect('/orders_tables')

