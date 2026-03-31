from django.shortcuts import render,redirect
from . models import Product, Transaction
from . forms import ProductForm, TransactionForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboard(request):
    products=Product.objects.all()

    query=request.GET.get('q')
    if query:
        products=products.filter(name__icontains=query)

    total_products=products.count()
    total_quantity=sum([p.quantity for p in products])

    low_stock=products.filter(quantity__lt=10)

    return render(request,'dashboard.html',{
        'products':products,       
        'total_products':total_products,
        'total_quantity':total_quantity,
        'low_stock':low_stock
        })

@login_required
def add_product(request):
    form=ProductForm(request.POST or None)
     
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'add_product.html',{'form':form})

@login_required
def edit_product(request,id):
    product=get_object_or_404(Product,id=id)
    form=ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request,'add_product.html',{'form':form})

@login_required
def delete_product(request,id):
    product=get_object_or_404(Product,id=id)
    product.delete()
    return redirect('dashboard')

@login_required
def add_transaction(request):
    form=TransactionForm(request.POST or None)

    if form.is_valid():
        transaction=form.save(commit=False)
        product=transaction.product
        qty=transaction.quantity

        if transaction.type=='IN':
            product.quantity+=qty
        else:
            if product.quantity<qty:
                return render(request,'add_transaction.html',{
                    'form':form,
                    'error':'Not enough stock!'
                })
            product.quantity -=qty

        product.save()
        transaction.save()

        return redirect('dashboard')
    return render(request,'add_transaction.html',{'form':form})

@login_required
def transaction_history(request):
    transactions=Transaction.objects.all().order_by('-date')
    return render(request,'transaction_history.html',{'transactions':transactions})