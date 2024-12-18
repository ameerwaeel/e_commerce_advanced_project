from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from cart.forms import CartAddProductForm

# Create your views here.
# def home(request):
#     context={'store':'store'}
#     return render(request,'home.html',context)

def list_products(request,slug=None):
    products = Product.objects.filter(status=Product.Status.AVAILABLE)
    category=None
    categories= Category.objects.all()
    if slug:
        category=get_object_or_404(Category, slug=slug)
        products=products.filter(category=category)

    context={'products':products,
             'categories':categories,
             'category':category

             }

    return render(request,'list_products.html',context)


  
# def products_detail(request,product_slug):
#     products = get_object_or_404(Product, slug=product_slug,status=Product.Status.AVAILABLE)
#     cart_product_form = CartAddProductForm()

#     context={'products':products,
#               'cart_product_form': cart_product_form,

#              }

#     return render(request,'products_detail.html',context)

def products_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    # print(f"Product Slug: {product.slug}")  # Debug line
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'products_detail.html', context)

def product_search(request):
    query=None
    results=[]
    if 'query' in request.GET:

        query=request.GET.get('query')
        search_query = SearchQuery(query)
        search_vector=SearchVector('name','description')
        results=Product.objects.annotate(search=search_vector,rank=SearchRank(search_vector,search_query)).filter(search=search_query,status=Product.Status.AVAILABLE).order_by('-rank')
    context={'query':query,
             'results':results}
    return render(request,'search.html',context)
