from django.contrib import admin
from .models import Contact, ServiceRequest, Request

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_id')

class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'address', 'contactnum')
    

class RequestAdmin(admin.ModelAdmin):
    list_display = ('id_number', 'name', 'service_type', 'status')
    # list_filter = ('service_type', 'initiated', 'pending')
    # search_fields = ('id_number', 'name')

# admin.site.register(Request, RequestAdmin)


admin.site.register(Contact, ContactAdmin)
admin.site.register(ServiceRequest, ServiceRequestAdmin)
admin.site.register(Request, RequestAdmin)
