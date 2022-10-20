from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key = True)
    productname= models.CharField(verbose_name='Mahsulot Nomi',max_length=300)
    price = models.IntegerField(verbose_name='Narxi',default=0,null=False)
    photo_id = models.CharField(verbose_name='Rasim uchun id',max_length=500,null=True)
    description = models.TextField(verbose_name='Mahsulot haqida',null=True)

    def __str__(self):
        return f"{self.id}-{self.productname}"

class Order(models.Model):
    id = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    


