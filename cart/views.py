from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django .views.decorators.http import require_POST

      
@require_POST
def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug, status=Product.Status.AVAILABLE)
    form = CartAddProductForm(request.POST)
    
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])

        return redirect('cart:cart_detail')
    else:
        return redirect('store:products_detail', product_slug=product.slug)


@require_POST
def cart_remove(request,product_slug) ->int:
    cart=Cart(request)
    product=get_object_or_404(Product,slug=product_slug,status=Product.Status.AVAILABLE)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart=Cart(request)
    cart_product_form=CartAddProductForm() 
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={
           'quantity':item['quantity'],
           'override':True 
        })
    context={
        'cart':cart,
        'cart_product_form':cart_product_form
    }
    return render(request,'cart_details.html',context)
