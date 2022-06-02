from unicodedata import category
from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)
# Register your models here.
