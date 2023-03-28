from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.reverse import reverse

from rest_framework import status
from rest_framework import permissions

from .models import AboutUs, FaQ, Product, ProductService, Company, ContactUsInfo, FormContactUs, TechService, TechCategory, TechPivotTable
from .serializers import AboutUsSerializer, FaQSerializer, ProductSerializer, ProductServiceSerializer, CompanySerializer, ContactUsSerializer, FormSerializer, TechCategorySerializer, TechServiceSerializer, TechPivotSerializer

class APIRoot(APIView):
    def get(self, request, format=None):
        data = {
            'about-us': reverse('about-list', request=request, format=format),
            'faq': reverse('faq-list', request=request, format=format),
            # Agrega aquí los demás endpoints de tu API
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

################################################### TECH CATEGORY SECTION ###################################################
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = TechCategory.objects.all()
    serializer_class = TechCategorySerializer

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechCategory.objects.all()
    serializer_class = TechCategorySerializer

################################################### TECH SERVICE SECTION ###################################################
class ServiceListCreateView(generics.ListCreateAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer

class ServiceRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechService.objects.all()
    serializer_class = TechServiceSerializer

################################################### PIVOT TABLE SECTION ###################################################
class TechPivotListCreateView(generics.ListCreateAPIView):
    queryset = TechPivotTable.objects.all()
    serializer_class = TechPivotSerializer

class TechPivotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TechPivotTable.objects.all()
    serializer_class = TechPivotSerializer

