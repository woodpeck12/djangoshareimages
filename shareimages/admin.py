from django.contrib import admin

# Register your models here.

from .models import ShareIamge

class WoodShareImage(admin.ModelAdmin):
    pass

admin.site.register(ShareIamge, WoodShareImage)