from django.shortcuts import render ,get_object_or_404,redirect
from .models import *
from .forms import *
from cart.cart import Cart
# for mail 
from django.core.mail import send_mail,EmailMessage
from django.conf import settings    
#for pdf order
from django .http import HttpResponse
import os
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
# import weasyprint


# @staff_member_required
# def admin_order_id(request,order_id):
#     order=get_object_or_404(Order,id=order_id)
#     html=render_to_string('pdf.html',{'order':order})
#     response=HttpResponse(content_type='application/pdf')
#     response['Content-Disposation']=f'filename=order{order.order_id}.pdf'
#     weasyprint.HTML(string=html).write_pdf(response)
#     return response



def order_create(request):
    cart=Cart(request)
    success=False
    if request.method == "POST":
        form=OrderCreateForm(request.POST)
        if form.is_valid():
            order=form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()  
            subject='order confirmation'
            message=f'your order id is :({order.order_id}) has been created successfuly \n \n order details:\n'
            for item in cart:
                product_name=item['product'].name
                # message += f'product : {product_name} , price :{item['price']} , quantity :{item['quantity']} \n  ' 
                message += f'Product: {product_name},\n Price: {item["price"]},\n Quantity: {item["quantity"]}\n'

            email_from=settings.DEFUALT_FROM_EMAIL
            recipient_list=[form.cleaned_data['email']]  
            send_mail(subject,message,email_from,recipient_list)  
            success=True
            return redirect('orders:order_pay_by_vodafon',order_id=order.id)

        return render(request,'created.html',{'order':order,'success':success})  
    else:
        form=OrderCreateForm()
    return render(request,'created.html',{'form':form,'cart':cart})  


def order_pay_by_vodafon(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    if request.method == 'POST':
        form = OrderPayForm(request.POST, request.FILES)
        if form.is_valid():
            order_pay = form.save(commit=False)
            order_pay.order = order
            order_pay.paied = True
            order_pay.save()
            return redirect('orders:payment_success', order_id=order.id)
    else:
        form = OrderPayForm()

    context={'order':order,
             'form':form,
             }        
    return render(request,'pay_form.html',context)        


def payment_success(request,order_id):
    order=get_object_or_404(Order,id=order_id)
    return render(request,'payment_success.html',{'order':order})
