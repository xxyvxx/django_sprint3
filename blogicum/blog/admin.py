# ice_cream/admin.py
from django.contrib import admin

# Register your models here.
from .models import Location
from .models import Category
from .models import Post

admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Post)
