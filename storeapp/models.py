from django.db import models

# Create your models here.



class BannerTop(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='banner_top_images',blank=True,null=True)

    def __str__(self) -> str:
        return self.name


class BannerDown(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='banner_down_images',blank=True,null=True)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='categoty_images',blank=True,null=True)


    def __str__(self) -> str:
        return self.name

class Product(models.Model):

    UNIT_GRAM = 'g'
    UNIT_KILOGRAM = 'kg'
    UNIT_NOS = 'Nos'
    UNIT_LITER='Ltr'

    UNIT_CHOICES = [

        (UNIT_GRAM, 'Gram'),(UNIT_KILOGRAM,'Kilogram'),(UNIT_NOS,'Nos'),(UNIT_LITER,'Ltr')

    ]


    name = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to='product_images',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    offer_price = models.CharField(max_length=255,blank=True,null=True)
    offer = models.CharField(max_length=255)
    unit =models.CharField(choices=UNIT_CHOICES,max_length=3)
    last_update=models.DateField(auto_now_add=True)



    def __str__(self) -> str:
        return self.name



    