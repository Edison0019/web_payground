from django.contrib import admin
from .models import Profile

# Register your models here.
class profileAdmin(admin.ModelAdmin):
    ordering = ('user',)
    readonly_fields = ('id',)
    
admin.site.register(Profile,profileAdmin)