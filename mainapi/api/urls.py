from rest_framework import routers

from django.urls import path, include
from .views import (
    APIRoot,

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

    TechnologyCategoryListCreateView,
    TechnologyCategoryRetrieveUpdateDestroyView,

    ServiceByTechnologyListCreateView,
    ServiceByTechnologyRetrieveUpdateDestroyView,

    TechPivotListCreateView,
    TechPivotRetrieveUpdateDestroyView,

    IndustryCategoryListCreateView,
    IndustryCategoryRetrieveUpdateDestroyView,

    ServiceByIndustryListCreateView,
    ServiceByIndustryRetrieveUpdateDestroyView,

    IndustryPivotListCreateView,
    IndustryPivotRetrieveUpdateDestroyView,
)


urlpatterns = [
    path('', APIRoot.as_view(), name='api-root'),

    path('company/', CompanyListApiView.as_view(), name='company-list'),

    path('about/', AboutListApiView.as_view(), name='about-list'),
    path('about/<int:aboutus_id>/', AboutUsDetailApiView.as_view(), name='aboutus-detail'),

    path('faq/', FaQListApiView.as_view(), name='faq-list'),
    path('faq/<int:faq_id>/', FaQDetailApiView.as_view()),

    path('product/', ProductApiView.as_view(), name='product-list'),
    path('product/service', ProductServiceApiView.as_view(), name='prodservice-list'),

    path('contact-us/', ContactUsView.as_view(), name='contact-us-list'),
    path('contact-us/<int:pk>/', ContactUsUpdateDestroyView.as_view(), name='contact-us-form'),

    path('contact-us-form/', FormListCreateView.as_view(), name='contact-us-form-list'),
    path('contact-us-form/<int:pk>/', FormsListUpdateDeleteView.as_view(), name='contact-us-form'),

    path('tech-category/', TechnologyCategoryListCreateView.as_view(), name='tech-category-list'),
    path('tech-category/<int:pk>/', TechnologyCategoryRetrieveUpdateDestroyView.as_view(), name='TechPivot_detail'),

    path('tech-service/', ServiceByTechnologyListCreateView.as_view(), name='tech-service-list'),
    path('tech-service/<int:pk>/', ServiceByTechnologyRetrieveUpdateDestroyView.as_view(), name='tech-service-detail'),    

    path('tech-pivot/', TechPivotListCreateView.as_view(), name='tech-pivot'),
    path('tech-pivot/<int:pk>/', TechPivotRetrieveUpdateDestroyView.as_view(), name='TechPivot_detail'),

    path('industry-category/', IndustryCategoryListCreateView.as_view(), name='industry-category-list'),
    path('industry-category/<int:pk>/', IndustryCategoryRetrieveUpdateDestroyView.as_view(), name='IndustryPivot_detail'),

    path('industry-service/', ServiceByIndustryListCreateView.as_view(), name='industry-service-list'),
    path('industry-service/<int:pk>/', ServiceByIndustryRetrieveUpdateDestroyView.as_view(), name='industry-service-detail'),    

    path('industry-pivot/', IndustryPivotListCreateView.as_view(), name='industry-pivot'),
    path('industry-pivot/<int:pk>/', IndustryPivotRetrieveUpdateDestroyView.as_view(), name='IndustryPivot_detail'),
]