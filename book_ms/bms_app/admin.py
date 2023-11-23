from django.contrib import admin
from .models import Books, Accessor

# Register your models here.
admin.site.register(Books)
admin.site.register(Accessor)