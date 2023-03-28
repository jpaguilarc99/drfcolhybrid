from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Company, AboutUs
from .serializers import CompanySerializer, AboutUsSerializer

# Company Testing
class CompanyListApiViewTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('company-list')
        Company.objects.create(company_name='Test Company', resources='Test Resources', logo='Test Logo')

    def test_list_companies(self):
        response = self.client.get(self.url)
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# About Us Testing
class AboutListApiViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client.force_authenticate(user=self.user)
        self.url = reverse('about-list')
        self.data = {
            'title': 'Test Title',
            'description': 'Test description',
            'about_image': 'test_image.jpg',
        }    
    
    def test_get_list(self):
        AboutUs.objects.create(**self.data)
        response = self.client.get(self.url)
        abouts = AboutUs.objects.all()
        serializer = AboutUsSerializer(abouts, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
    def test_create_about(self):
        response = self.client.post(self.url, data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        about = AboutUs.objects.first()
        self.assertEqual(about.title, self.data['title'])
        self.assertEqual(about.description, self.data['description'])
        self.assertEqual(about.about_image, self.data['about_image'])
        
    def test_create_invalid_about(self):
        data = {
            'title': '',
            'description': '',
            'about_image': '',
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)