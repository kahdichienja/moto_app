from django.db import models

# Create your models here.
class Category(models.Model):
    """Model definition for Category."""
    category_name = models.CharField(max_length = 191)

    # TODO: Define fields here
    def __str__(self):
        """Unicode representation of Category."""
        return f'{self.category_name}'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    number_in_stock = models.IntegerField()
    product_name = models.CharField(max_length = 191)
    product_price = models.FloatField()
    description = models.TextField()
    product_photo = models.FileField(upload_to='Products')
    timestamp = models.DateTimeField(auto_now = True)
    is_reserved = models.BooleanField(null = True)
    is_sold_out = models.BooleanField(null = True)
    is_new = models.BooleanField(null = True)
    is_under_nego = models.BooleanField(null = True)

    def __str__(self):
        return f'{self.product_name}'

class ProductAttribute(models.Model):
    """Model definition for ProductAttribute."""

    # TODO: Define fields here
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attrbute_photo = models.FileField(upload_to='ProductAttribute')

    def __str__(self):
        """Unicode representation of ProductAttribute."""
        return f'{self.product} Attribute'
