from rest_framework import routers

from django.urls import path, include
from .views import (
    AboutListApiView,
    AboutUsDetailApiView,

    FaQListApiView,
    FaQDetailApiView,

    ProductApiView,
    ProductServiceApiView,

    CompanyListApiView,

    ContactUsView,
    ContactUsUpdateDestroyView,

    FormListCreateView,
    FormsListUpdateDeleteView,

    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,

    ServiceListCreateView,
    ServiceRetrieveUpdateDestroyView,

    TechPivotListCreateView,
    TechPivotRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('company/', CompanyListApiView.as_view(), name='company-list'),

    path('about/', AboutListApiView.as_view(), name='about-list'),
    path('about/<int:aboutus_id>/', AboutUsDetailApiView.as_view(), name='aboutus-detail'),

    path('faq/', FaQListApiView.as_view(), name='faq-list'),
    path('faq/<int:faq_id>/', FaQDetailApiView.as_view()),

    path('product/', ProductApiView.as_view(), name='product-list'),
    path('product/service', ProductServiceApiView.as_view()),

    path('contact-us/', ContactUsView.as_view(), name='contact-us-list'),
    path('contact-us/<int:pk>/', ContactUsUpdateDestroyView.as_view(), name='contact-us-form'),

    path('contact-us-form/', FormListCreateView.as_view(), name='contact-us-list'),
    path('contact-us-form/<int:pk>/', FormsListUpdateDeleteView.as_view(), name='contact-us-form'),

    path('tech-service/', ServiceListCreateView.as_view(), name='service_create'),
    path('tech-service/<int:pk>/', ServiceRetrieveUpdateDestroyView.as_view(), name='service_detail'),

    path('tech-category/', CategoryListCreateView.as_view(), name='service_create'),
    path('tech-category/<int:pk>/', CategoryRetrieveUpdateDestroyView.as_view(), name='TechPivot_detail'),

    path('tech-pivot/', TechPivotListCreateView.as_view(), name='service_create'),
    path('tech-pivot/<int:pk>/', TechPivotRetrieveUpdateDestroyView.as_view(), name='TechPivot_detail'),
]