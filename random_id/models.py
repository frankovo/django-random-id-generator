import random
import string

from django.db import models

from random_id.utils import generate_random_string as id_generator

class Product(models.Model):
    order_id = models.CharField('Article Refrence', max_length=11, editable=False, unique=True, null=True)
    article_name = models.CharField("Article name", max_length=128) 

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.article_name
     
    def save(self):
        if not self.order_id:
            # Generate ID once, then check the db. If exists, keep trying.
            self.order_id = id_generator()
            while Product.objects.filter(order_id=self.order_id).exists():
                self.order_id = id_generator()
        super(Product, self).save()

