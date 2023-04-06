from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.reverse import reverse

from rest_framework import status
from rest_framework import permissions

from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, TechCategory, ServiceByTechnology, ServiceTechnologyPivot, IndustryCategory, ServiceByIndustry, ServiceIndustryPivot
from .serializers import AboutUsSerializer, FaQSerializer, ProductSerializer, ProductServiceSerializer, CompanySerializer, ContactUsSerializer, FormSerializer, TechCategorySerializer, ServiceByTechnologySerializer, ServiceTechnologyPivotSerializer, IndustryCategorySerializer, ServiceByIndustrySerializer, ServiceIndustryPivotSerializer

class APIRoot(APIView):
    def get(self, request, format=None):
        data = {
            'company': reverse('company-list', request=request, format=format),

            'about-us': reverse('about-list', request=request, format=format),

            'faq': reverse('faq-list', request=request, format=format),

            'featured-products': reverse('product-list', request=request, format=format),
            'featured-products-services': reverse('prodservice-list', request=request, format=format),

            'contact-us': reverse('contact-us-list', request=request, format=format),
            'contact-us-form': reverse('contact-us-form-list', request=request, format=format),

            'tech-service': reverse('tech-service-list', request=request, format=format),
            'tech-category': reverse('tech-category-list', request=request, format=format),   
            'tech-pivot': reverse('tech-pivot', request=request, format=format),    

            'industry-service': reverse('industry-service-list', request=request, format=format),
            'industry-category': reverse('industry-category-list', request=request, format=format),   
            'industry-pivot': reverse('industry-pivot', request=request, format=format),       
        }
        return Response(data)

################################################### COMPANY INFO SECTION ###################################################
# Company Info List API View

class CompanyListApiView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

################################################### ABOUT US SECTION ###################################################

# About List API View
class AboutListApiView(APIView):
    # Permissions 
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the aboutus items for given requested user
        '''
        abouts = AboutUs.objects.all()
        serializer = AboutUsSerializer(abouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the About Us with given abouts data
        '''
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),  
            'about_image': request.data.get('about_image')          
        }
        serializer = AboutUsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Detail About List API View
class AboutUsDetailApiView(APIView):
    #Authentications
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, aboutus_id, user_id):
        """
        Helper method to get the object with given about_id
        """
        try:
            return AboutUs.objects.get(id=aboutus_id)
        except AboutUs.DoesNotExist:
            return None
        
    #GET method
    def get(self, request, aboutus_id, *args, **kwargs):
        """
        Retrieves About with given about_id
        """
        about_instance = self.get_object(aboutus_id, request.user.id)
        if not about_instance:
            return Response(
                {"response":"Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = AboutUsSerializer(about_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #PUT method
    def put(self, request, aboutus_id, *args, **kwargs):
        """
        Updates the about item wt given about_id 
        """
        about_instance = self.get_object(aboutus_id, request.user.id)
        if not about_instance:
            return Response(
                {"response":"Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )        
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description')            
        }
        serializer = AboutUsSerializer(instance=about_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE method
    def delete(self, request, aboutus_id, *args, **kwargs):
        """
        Deletes the about item wt given about_id if exists
        """
        about_instance = self.get_object(aboutus_id, request.user.id)
        if not about_instance:
            return Response(
                {"response": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        about_instance.delete()
        return Response(
            {"response": "Object deleted!"},
            status=status.HTTP_200_OK
        )

################################################### FAQ SECTION ###################################################
# FaQ List API View
class FaQListApiView(APIView):
    # Permissions 
    #permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        List all the FaQ items for given requested user
        '''
        faqs = FaQ.objects.all()
        serializer = FaQSerializer(faqs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        '''
        Create the FaQ with given faqs data
        '''
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),  
            'issue_link': request.data.get('issue_link')          
        }
        serializer = FaQSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Detail FaQ List API View 
class FaQDetailApiView(APIView):
    #Authentications
    #permission_classes = [permissions.IsAuthenticated]

    def get_object(self, faq_id, user_id):
        """
        Helper method to get the object with given faq_id
        """
        return FaQ.objects.filter(id=faq_id).first()        
        
    #GET method
    def get(self, request, faq_id, *args, **kwargs):
        """
        Retrieves About with given faq_id
        """
        faq_instance = self.get_object(faq_id, request.user.id) or \
               Response({"response":"Object does not exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = FaQSerializer(faq_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #PUT method
    def put(self, request, faq_id, *args, **kwargs):
        """
        Update FAQ item with given ID
        """
        faq_instance = self.get_object(faq_id, request.user.id)
        if not faq_instance:
            return Response({'response': 'Object does not exists'}, status=status.HTTP_400_BAD_REQUEST)   
            
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description')            
        }

        serializer = FaQSerializer(instance=faq_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #DELETE method
    def delete(self, request, faq_id, *args, **kwargs):
        """
        Deletes the about item wt given about_id if exists
        """
        faq_instance = self.get_object(faq_id, request.user.id) or None

        if not faq_instance:
            return Response(
                {"response": "Object does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        faq_instance.delete()

        return Response(
            {"response": "Object deleted!"},
            status=status.HTTP_200_OK
        )

################################################### FEATURED SECTION ###################################################
class ProductApiView(generics.ListAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer

class ProductServiceApiView(generics.ListAPIView):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer


################################################### CONTACT US SECTION ###################################################
class ContactUsView(generics.ListCreateAPIView):
    queryset = ContactUsInfo.objects.all()
    serializer_class = ContactUsSerializer

class ContactUsUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContactUsInfo.objects.all()
    serializer_class = ContactUsSerializer

################################################### FORM LIST SECTION ###################################################
class FormListCreateView(generics.ListCreateAPIView):
    queryset = FormContactUs.objects.all()
    serializer_class = FormSerializer

class FormsListUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FormContactUs.objects.all()
    serializer_class = FormSerializer

################################################### TECHNOLOGY CATEGORY SECTION ###################################################
class TechnologyCategoryListCreateView(generics.ListCreateAPIView):
    queryset = TechCategory.objects.all()
    serializer_class = TechCategorySerializer

class TechnologyCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechCategory.objects.all()
    serializer_class = TechCategorySerializer

################################################### SERVICE BY TECHNOLOGY SECTION ###################################################
class ServiceByTechnologyListCreateView(generics.ListCreateAPIView):
    queryset = ServiceByTechnology.objects.all()
    serializer_class = ServiceByTechnologySerializer

class ServiceByTechnologyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceByTechnology.objects.all()
    serializer_class = ServiceByTechnologySerializer

################################################### SERVICE TECHNOLOGY PIVOT TABLE SECTION ###################################################
class TechPivotListCreateView(generics.ListCreateAPIView):
    queryset = ServiceTechnologyPivot.objects.all()
    serializer_class = ServiceTechnologyPivotSerializer

class TechPivotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTechnologyPivot.objects.all()
    serializer_class = ServiceTechnologyPivotSerializer


################################################### INDUSTRY CATEGORY SECTION ###################################################
class IndustryCategoryListCreateView(generics.ListCreateAPIView):
    queryset = IndustryCategory.objects.all()
    serializer_class = IndustryCategorySerializer

class IndustryCategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndustryCategory.objects.all()
    serializer_class = TechCategorySerializer

################################################### SERVICE BY INDUSTRY SECTION ###################################################
class ServiceByIndustryListCreateView(generics.ListCreateAPIView):
    queryset = ServiceByIndustry.objects.all()
    serializer_class = ServiceByIndustrySerializer

class ServiceByIndustryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceByIndustry.objects.all()
    serializer_class = ServiceByIndustrySerializer

################################################### SERVICE INDUSTRY PIVOT TABLE SECTION ###################################################
class IndustryPivotListCreateView(generics.ListCreateAPIView):
    queryset = ServiceIndustryPivot.objects.all()
    serializer_class = ServiceIndustryPivotSerializer

class IndustryPivotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceTechnologyPivot.objects.all()
    serializer_class = ServiceIndustryPivotSerializer