from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.db.models.signals import pre_save, post_save, m2m_changed
# Create your models here.

class CartManager(models.Manager):

    def new_or_get(self, request, id):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id = cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first() 
            if request.user.is_authenticated and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = Cart.objects.new(user=request.user)
            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj
        # cart_obj, new_obj = Cart.objects.new_or_get(request, id)
    # products = cart_obj.product.all()
    # total = 0
    # for x in products:
    #     total += x.product_price
    #     print(total)
    # cart_obj.total = total
    # cart_obj.save()
    def new(self, user = None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    """Model definition for Cart."""

    # TODO: Define fields here
    user    = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, blank=True, on_delete=models.CASCADE)
    total   = models.DecimalField(default = 0.00, max_digits=100, decimal_places=2)
    qnty    = models.IntegerField(default = 1)
    updated = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField(auto_now_add = True)

    # objects = CartManager()

    def __str__(self):
        """Unicode representation of Cart."""
        return f'{self.id}'
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    country = models.CharField(max_length=50)
    address = models.TextField()
    town_city = models.CharField(max_length=50)
    county_state = models.CharField(max_length=50)
    postal_zip = models.CharField(max_length=50)
    is_paid = models.CharField(default = 'Pending', max_length=50)
    when_to_contact_u = models.CharField(max_length=50, blank = True, null = True)

    def __str__(self):
        return f'{self.user} : {self.phone_number}'
