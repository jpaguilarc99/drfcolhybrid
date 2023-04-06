from rest_framework import serializers
from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, TechCategory, ServiceByTechnology, ServiceTechnologyPivot, IndustryCategory, ServiceByIndustry, ServiceIndustryPivot

### Agui

#About Us Serializer
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

#FaQ Serializer
class FaQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaQ
        fields = '__all__'

#Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

#Product Service Serializer
class ProductServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductService
        fields = '__all__'

#Company Serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


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

#Technology Category Serializer
class TechCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TechCategory
        fields = '__all__'

#Service By Technology Serializer
class ServiceByTechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceByTechnology
        fields = '__all__'

#Service by Technology Pivot Serializer
class ServiceTechnologyPivotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceTechnologyPivot
        fields = '__all__'      

#Industry Category Serializer
class IndustryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCategory
        fields = '__all__'

#Service by Industry Serializer
class ServiceByIndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceByIndustry
        fields = '__all__'

#Service by Industry Pivot Serializer
class ServiceIndustryPivotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceIndustryPivot
        fields = '__all__'    
