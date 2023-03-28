from django.db import models
from django.contrib.auth.models import User

#About Us Model
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    about_image = models.CharField(max_length=200)    

    def __str__(self):
        return self.title

#FaQ Model
class FaQ(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    issue_link = models.CharField(max_length=200)

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


    def __str__(self):
        return self.firstname

#Tech Category Model
class TechCategory(models.Model):
    name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.name

#Tech Service Model
class TechService(models.Model):
    name = models.CharField(max_length=100)    

    def __str__(self):
        return self.name

#Pivot Table Tech Service/Tech Category
class TechPivotTable(models.Model):
    service_id=  models.ForeignKey(TechService, on_delete=models.CASCADE)
    category_id = models.ForeignKey(TechCategory, on_delete=models.CASCADE)