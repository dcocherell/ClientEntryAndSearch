from django.contrib import admin
from .models import Client

# Register your models here.

admin.site.site_header = 'Client Database Administration'  # Set the admin header

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zip', 'status')
    search_fields = ('first_name', 'last_name', 'email', 'phone')  # Define searchable fields

admin.site.register(Client, ClientAdmin)