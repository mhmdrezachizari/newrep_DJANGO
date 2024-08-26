from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=False,)
    def __str__(self):
        return self.name
class PRODUCTS(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    category = models.ManyToManyField(Category, related_name='category')
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    increadibleoffer = models.BooleanField(default=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def get_category(self):
        return ", ".join([cat.title for cat in self.category.all()])
class TOPVBANNER(models.Model):
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    name = models.CharField(max_length=100)
class FORMSSEARCHMODEL(models.Model):
    name = models.CharField(max_length=100 , blank=True)
    def __str__(self):
        return self.name

