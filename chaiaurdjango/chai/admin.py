from django.contrib import admin
from .models import chaiVarity, chaiReview, Store, chaiCertificate

# Register your models here.

class chaiReviewInline(admin.TabularInline):
    model = chaiReview
    extra = 1

class chaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price', 'date_added')
    inlines = [chaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_vareties',)
    
class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date', 'expiry_date') 


   
admin.site.register(chaiVarity, chaiVarityAdmin)

admin.site.register(Store, StoreAdmin)

admin.site.register(chaiCertificate, chaiCertificateAdmin)