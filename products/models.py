from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category Model from CI Boutique Ado
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)
    friendly_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Product Model modified from CI Boutique Ado
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    has_colour = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.DecimalField(max_digits=3, decimal_places=0, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    available = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, related_name='favourites',
                                        blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        """
        Newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return self.name
