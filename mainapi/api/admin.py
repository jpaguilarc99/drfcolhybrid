from django.contrib import admin

from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, ServiceByTechnology, TechCategory, ServiceTechnologyPivot, ServiceByIndustry, IndustryCategory, ServiceIndustryPivot

# Register your models here.
admin.site.register(AboutUs)

admin.site.register(FaQ)

admin.site.register(Product)
admin.site.register(ProductService)

admin.site.register(Company)

admin.site.register(ContactUsInfo)
admin.site.register(FormContactUs)

admin.site.register(ServiceByTechnology)
admin.site.register(TechCategory)
admin.site.register(ServiceTechnologyPivot)

admin.site.register(ServiceByIndustry)
admin.site.register(IndustryCategory)
admin.site.register(ServiceIndustryPivot)