from django.test import TestCase
from django.urls import resolve
from lists.views import home_page#(2)
from django.http import HttpRequest
from django.template.loader import render_to_string
class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response= self.client.get('/')#1
        self.assertTemplateUsed(response,'home.html')#3
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/',data={'item_text':'A new list item'})
        self.assertIn('A new list item',response.content.decode())
        self.assertTemplateUsed(response,'home.html')
# Create your tests here.