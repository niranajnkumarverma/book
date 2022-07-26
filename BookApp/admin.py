from django.contrib import admin
from .views import app_info
from .models import *

class SuperAdmin(admin.ModelAdmin):
    admin.site.site_header = admin.site.site_title = app_info['app_name']
    admin.site.index_title = f"{app_info['app_name']}'s Admin"
    admin.site.site_header = "My User portal"
    search_fields = ("last_name__startswith", ) 
    empty_value_display = '-empty-'
    list_per_page = 10    

admin.site.register(User, SuperAdmin)
admin.site.register(Product, SuperAdmin)
admin.site.register(WishList, SuperAdmin)
admin.site.register(Cart, SuperAdmin)
admin.site.register(Transaction, SuperAdmin)