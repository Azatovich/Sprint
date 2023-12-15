from django.contrib import admin
from .models import Routes, Category, User, Level, Coords

# Register your models here.

admin.site.register(Routes)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Level)
admin.site.register(Coords)