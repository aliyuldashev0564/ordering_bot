from django.contrib import admin
from . import models
from django.contrib.auth.models import Group, User
# Register your models here.


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(models.agent)
admin.site.register(models.product)
class ord(admin.ModelAdmin):
    search_fields = ('client_name',)
    list_filter = ('time', 'agent')
    exclude = ['id','is_active','refused','time']
    list_display = ['agent','to_product','money']
admin.site.register(models.orders, ord)

