from django.db import models

# Create your models here.
class Category(models.Model):
    tittle = models.CharField(max_length = 255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.tittle

class Book(models.Model):
    tittle = models.CharField(max_length=155)
    category = models.ForeignKey(Category,related_name='books',on_delete =models.CASCADE)
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.IntegerField()
    stocks = models.IntegerField()
    description = models.TextField()
    imageURl = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.tittle


    

    def __str__(self):
        return self.tittle
    
class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category,related_name='delete', on_delete=models.CASCADE)
    price = models.IntegerField()
    stocks = models.IntegerField()
    imageURL = models.URLField()
    status = models.BooleanField()
    date_created = models.DateField(auto_now_add=True)

    class meta:
        ordering =['-date_created']
    def __str__(self):
        return '{} {}'.format(self.product_tag,self.name)
    

    

