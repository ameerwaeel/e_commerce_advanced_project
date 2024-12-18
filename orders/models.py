from django.db import models
import random
import string
from django.utils.timezone import now as timezone_now
from store.models import *
# Create your models here.
def genrate_order_id(length=8):
    characters=string.ascii_letters+string.digits
    return ''.join(random.choices(characters,k=length))

class Order(models.Model):
    order_id=models.CharField(max_length=8,default=genrate_order_id,unique=True)
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    adress=models.CharField( max_length=50)
    postal_code=models.PositiveIntegerField()
    city=models.CharField( max_length=50)
    created_at=models.DateTimeField(default=timezone_now)
    updated_at=models.DateTimeField( auto_now=True)
    paied=models.BooleanField(default=False)


    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")
        ordering=['-created_at']
        indexes=[models.Index(fields=['-created_at'])]

    def __str__(self):
        return str(self.order_id)
    def save(self,*args, **kwargs):
        if not self.order_id:
            unique_id=genrate_order_id()
            while Order.objects.filter(order_id=unique_id).exists():
                unique_id=genrate_order_id()
                self.order_id=unique_id
        super().save(*args, **kwargs)        


    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
        
    # def get_absolute_url(self):
    #     return reverse("Order_detail", kwargs={"pk": self.pk})

class OrderItem(models.Model):
    order=models.ForeignKey(Order,related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, related_name='order_item', on_delete=models.CASCADE)
    price=models.DecimalField( max_digits=6, decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    

    class Meta:
        verbose_name = ("OrderItem")
        verbose_name_plural = ("OrderItems")

    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity
    # def get_absolute_url(self):
    #     return reverse("OrderItem_detail", kwargs={"pk": self.pk})



class OrderPay(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    pay_phone=models.CharField( max_length=11)
    pay_image=models.ImageField( upload_to='vodavon_cash' )
    created=models.DateTimeField( auto_now_add=True)

 
    class Meta:
        verbose_name = ("OrderPay")
        verbose_name_plural = ("OrderPays")
        ordering=['-created']


    def __str__(self):
        return str(self.order.order_id)

    # def get_absolute_url(self):
    #     return reverse("OrderPay_detail", kwargs={"pk": self.pk})
