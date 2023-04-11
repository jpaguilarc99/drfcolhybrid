from django.db import models
from django.contrib.auth.models import User

#About Us Model
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    about_image = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "About us"    

    def __str__(self):
        return self.title

#FaQ Model
class FaQ(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_link = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "FaQs"  

    def __str__(self):
        return self.title

#Featured Product Model
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()

    def __str__(self):
        return self.product_name

#Service by featured product Model
class ProductService(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.TextField()
    product_id = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        default= None,
    )

    def __str__(self):
        return self.service_name

#Company info Model
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    resources = models.CharField(max_length=200)
    logo = models.CharField(max_length=250)

    def __str__(self):
        return self.company_name

#Contact Us Model
class ContactUsInfo(models.Model):
    location = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=200)
    cellphone= models.TextField()
    email = models.TextField()
    images = models.TextField()

    class Meta:
        verbose_name_plural = "Contact us"  

    def __str__(self):
        return self.location

#FormContactUs Model
class FormContactUs(models.Model):

    FORM_TYPE_CHOICES = [
        ('question', 'Question'),
        ('consultation', 'Consultation'),
    ]

    COSTUMER_TYPE_CHOICES = [
        ('personal', 'Personal'),
        ('business', 'Business'),
    ]


    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=50)
    email = models.TextField()
    contactway = models.TextField(blank=True, null=True)
    message = models.TextField()
    countrycode = models.CharField(max_length= 4)
    phonenumber = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    consultdate = models.DateField(blank=True, null=True)
    formtype = models.CharField( max_length=30,choices=FORM_TYPE_CHOICES)
    costumertype = models.CharField( max_length=30,choices=COSTUMER_TYPE_CHOICES, null=True)

    class Meta:
        verbose_name_plural = "Form contact us"  

    def __str__(self):
        return self.firstname

#Technology Category Model
class TechCategory(models.Model):

    category_name = models.CharField(max_length=100, default='default_category_name')
    description_tech = models.TextField()

    class Meta:
        verbose_name_plural = "Categories by Technology"

    def __str__(self):
        return self.category_name

#Service By Technology Model  
class ServiceByTechnology(models.Model):
    
    service_name = models.CharField(max_length=100, default='default_service_name')
    service_description = models.TextField(default="")
    short_description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Service by Technology"

    def __str__(self):
        return self.service_name

#Service By Technology Pivot Model
class ServiceTechnologyPivot(models.Model):
    tech_category_id = models.ForeignKey(
        'TechCategory',
        on_delete=models.CASCADE,
        default= None,
    )

    service_technology_id = models.ForeignKey(
        'ServiceByTechnology',
        on_delete=models.CASCADE,
        default= None,
    )

#Industry Category Model
class IndustryCategory(models.Model):

    category_name = models.CharField(max_length=100, default='default_category_name')
    description_industry = models.TextField(default="")

    class Meta:
        verbose_name_plural = "Categories by Industry"

    def __str__(self):
        return self.category_name

#Service By Industry Model  
class ServiceByIndustry(models.Model):
    
    service_name = models.CharField(max_length=100, default='default_serv_name')
    service_description = models.TextField(default=True)
    short_description = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = "Service by Industry"

    def __str__(self):
        return self.service_name

#Service By Industry Pivot Model
class ServiceIndustryPivot(models.Model):
    industry_category_id = models.ForeignKey(
        'IndustryCategory',
        on_delete=models.CASCADE,
        default= None,
    )

    service_industry_id = models.ForeignKey(
        'ServiceByIndustry',
        on_delete=models.CASCADE,
        default= None,
    )