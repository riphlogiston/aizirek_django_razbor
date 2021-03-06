from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Category(models.Model):
    title=models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.title
    
class Product(models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    #Category.objects.all(products=product_id)
    image=models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.title


class Product_Image(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images')
    image=models.ImageField(upload_to='products/', blank=True, null=True)

class Review (models.Model):
    author=models.ForeignKey(User, on_delete=models.CASCADE,related_name='reviews')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='reviews')
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('-created_at',)

    def __str__(self):
        return f'{self.author.email}'

class Likes (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='likes')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='likes')
    is_liked=models.BooleanField(default=False)

class Favourite (models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='favourites')
    product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='favourites')
    favourite=models.BooleanField(default=False)
    


    