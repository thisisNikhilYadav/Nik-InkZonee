from django.db import models

# Create your models here.
class Carousel(models.Model):
    image = models.ImageField(upload_to='myapp/images/carousel',default='')
    label = models.CharField(max_length=25)
    content = models.CharField(max_length=100)
    
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=75)
    desc=models.CharField(max_length=500,default='')
    price=models.CharField(max_length=50,default=0)
    image=models.ImageField(upload_to='myapp/images',default='')

    def __str__(self):
        return self.product_name
    

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True,default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.BigIntegerField(default='')
    desc = models.TextField(default='')

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    post_id = models.AutoField(primary_key=True)
    title=models.CharField(max_length=75)
    heading1=models.CharField(max_length=100,default='')
    cheading1=models.CharField(max_length=5000,default='')
    heading2=models.CharField(max_length=100,default='')
    cheading2=models.CharField(max_length=5000,default='')
    heading3=models.CharField(max_length=1000,default='')
    cheading3=models.CharField(max_length=5000,default='')
    pub_date=models.DateField()
    thumbnail=models.ImageField(upload_to='myapp/images/blog',default='')
    author=models.CharField(max_length=75,default='')

    def __str__(self):
        return self.title