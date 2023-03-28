from django.contrib import admin

from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, TechService, TechCategory, TechPivotTable

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(FaQ)
admin.site.register(Product)
admin.site.register(ProductService)
admin.site.register(Company)
admin.site.register(ContactUsInfo)
admin.site.register(FormContactUs)
admin.site.register(TechService)
admin.site.register(TechCategory)
admin.site.register(TechPivotTable)