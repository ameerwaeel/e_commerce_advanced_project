from django.db import models
from django.utils.translation import gettext_lazy  as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField( max_length=50)
    slug=models.SlugField(blank=True,null=True)
    created=models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def get_category_url(self):
        return reverse("store:category_detail", kwargs={"slug": self.slug})
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super(Category,self).save(*args, **kwargs)
    
class Product(models.Model):
    # class status(models.TextChoices):
    #     AVALIABLE='av','avaliable'
    #     DREFT='df','dreft'
    class Status(models.TextChoices):
        AVAILABLE = 'av', 'Available'  # Correct spelling
        DRAFT = 'df', 'Draft'
    
    name=models.CharField( max_length=50)
    slug=models.SlugField(blank=True,null=True)
    image=models.ImageField( upload_to='products/images')
    description=models.TextField(max_length=500)
    price=models.DecimalField( max_digits=6, decimal_places=2)
    status = models.CharField(max_length=2, choices=Status.choices)
    created_at=models.DateTimeField( auto_now_add=True)
    update=models.DateTimeField( auto_now_add=True)
    category=models.ForeignKey('Category',  on_delete=models.CASCADE,blank=True,null=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        return super(Product,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.name

    def get_products_url(self):
        return reverse("store:products_detail", kwargs={"product_slug": self.slug})

    class Meta:
        ordering=['name']
        indexes=[models.Index(fields=['id','slug']),
                  models.Index(fields=['name']),
                  models.Index(fields=['-created_at'])         
                 ]
