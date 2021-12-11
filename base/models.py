from django.db import models

class Color(models.Model):
    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    options = (
        ('red', 'Red'),
        ('black', 'Black'),
        ('blue','Blue'),
    )

    name = models.CharField(max_length=100)
    model = models.CharField(null=True,blank=True,max_length=50)
    brand = models.CharField(null=True,blank=True,max_length=50)
    color = models.CharField(max_length=20,choices=options, default='black')
    unit_price = models.FloatField()
    current_stock = models.IntegerField(default=10,null=True,blank=True)
    image = models.FileField(blank=True,null=True,upload_to='products')
    details = models.TextField()

    def __str__(self):
        return self.name

