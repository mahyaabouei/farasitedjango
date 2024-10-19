from django.contrib import admin
from .models import SuperProduct, SubSuperProduct


admin.site.register(SubSuperProduct)
admin.site.register(SuperProduct)
