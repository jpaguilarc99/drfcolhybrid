from rest_framework import serializers
from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, TechCategory, TechService, TechPivotTable

### Agui

#About Us Serializer
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ("title", "description", "timestamp", "about_image")

#FaQ Serializer
class FaQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaQ
        fields = ("title", "description", "issue_link")

#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("product_name", "product_description")

#Product Service Serializer
class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = ("service_name", "service_description")

#Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("company_name", "resources", "logo")


### Macha

#Contact Us Serializer
class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUsInfo
        fields = '__all__'

#Form Serializer
class FormSerializer(serializers.ModelSerializer):
    contactway = serializers.JSONField()

    class Meta:
        model = FormContactUs
        fields = '__all__'

    consultdate = serializers.DateField(required=False, allow_null=True)

    def validate(self, data):
        formtype = data.get('formtype')
        consultdate = data.get('consultdate')

        if formtype == 'consultation' and not consultdate:
            raise serializers.ValidationError('Consultation date is required')

        if formtype == 'question' and consultdate:
            raise serializers.ValidationError('Consultation date should not be provided for a question')

        return data

    def validate_formtype(self, value):
        allowed_formtype = [choice[0] for choice in FormContactUs.FORM_TYPE_CHOICES]
        if value not in allowed_formtype:
            raise serializers.ValidationError("Invalid Data.")
        return value
    def validate_costumertype(self, value):
        allowed_costumertype = [choice[0] for choice in FormContactUs.COSTUMER_TYPE_CHOICES]
        if value not in allowed_costumertype:
            raise serializers.ValidationError("Invalid Data.")
        return value

#Tech Service Serializer
class TechServiceSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True)

    class Meta:
        model = TechService
        fields = '__all__'

#Tech Category Serializer
class TechCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCategory
        fields = '__all__'

#Tech Pivot Serializer
class TechPivotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechPivotTable
        fields = '__all__'       
