from django.contrib import admin

# Register your models here.
from .models import Item, Header

admin.site.register(Item)
admin.site.register(Header)