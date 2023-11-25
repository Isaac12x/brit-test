from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model


User = get_user_model()


class Cart(models.Model):
    """ 
        !Disclaimer: 
        Implementation of total_amount being perishable; so it expires after a certain time.
        The closest modelling of this is to have a Cart model that has a total_amount field
        computed from the items in the cart
    """
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name

    @property
    def total_amount(self):
        return self.items.aggregate(
            total=models.Sum(F('quantity') * F('price'), output_field=models.DecimalField())
        )['total'] or 0


# alternative implementation of the Summary
class Summary(models.Model):
    """ 
        !Disclaimer:
        This is an alternative implementation of the Summary model.
        Where the total_amount is persistent and only updates when the items change.
    """
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    quantity = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.name

    def calculate_amount(self):
        self.total_amount = self.quantity * self.item.price
        self.save()