from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model


User = get_user_model()


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', related_name='cart_items', on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"


class Cart(models.Model):
    """ 
        !Disclaimer: 
        Implementation of total_amount being perishable; so it expires after a certain time.
        The closest modelling of this is to have a Cart model that has a total_amount field
        computed from the items in the cart
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Summary for {self.user.username}"

    @property
    def total_amount(self):
        return self.cart_items.aggregate(
            total=models.Sum(F('quantity') * F('item__price'), output_field=models.DecimalField())
        )['total'] or 0


# alternative implementation of the Summary
class Summary(models.Model):
    """ 
        !Disclaimer:
        This is an alternative implementation of the Summary model.
        Where the total_amount is persistent and only updates when the items change.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name

    def calculate_amount(self):
        self.total_amount = sum(each.quanity * each.price for each in self.cart_items)
        self.save()