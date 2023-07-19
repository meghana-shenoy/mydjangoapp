from django.contrib import admin

# Register your models here.
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    # Let you to search with first name, last name and phone number of the customer
    search_fields = ['firstname', 'lastname', 'mobile']
    # There will be a filter on first name
    list_filter = ['firstname']
    list_display = ("firstname","lastname","mobile")
 
admin.site.register(Contact,ContactAdmin) 