from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from random_id.utils import generate_random_string as id_generator


@python_2_unicode_compatible
class Product(models.Model):
    order_id = models.CharField(
        'Article Refrence', max_length=11,
        editable=False, unique=True, null=True)
    article_name = models.CharField("Article name", max_length=128)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.article_name

    def save(self):
        if not self.order_id:
            # Generate ID once, then check the database. If exists, keep trying.
            self.order_id = id_generator()
            while Product.objects.filter(order_id=self.order_id).exists():
                self.order_id = id_generator()
        super(Product, self).save()
