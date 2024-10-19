from django.contrib import admin

from . import models

admin.site.register(models.Introduction)
admin.site.register(models.Content)
admin.site.register(models.Card)
admin.site.register(models.Sections)

