from django.test import TestCase
from .models import Company

# Testing Company Model
class CompanyModelTest(TestCase):
    def setUp(self):
        self.company = Company.objects.create(
            company_name='Company Name',
            resources='Resources',
            logo='Logo'
        )

    def test_company_name(self):
        company_name = self.company.company_name
        self.assertEqual(company_name, 'Company Name')

    def test_resources(self):
        resources = self.company.resources
        self.assertEqual(resources, 'Resources')

    def test_logo(self):
        logo = self.company.logo
        self.assertEqual(logo, 'Logo')
