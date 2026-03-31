from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.FloatField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    TRANSACTION_TYPE=(
        ('IN','Stock IN'),
        ('OUT','Stock Out')
    )

    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    type=models.CharField(max_length=3,choices=TRANSACTION_TYPE)
    quantity=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
