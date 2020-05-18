from django.test import TestCase

# Create your tests here.

from django.urls import reverse # new

from .models import Post

class PostModelTest(TestCase):
    
    ...
    
class HomePageView(TestCase): # new
    
    def setUp(self):
        
        Post.objects.create(text='this is another test')
        
    def test_view_url_exists_at_proper_location(self):
        
        resp = self.client.get('/')
        
        self.assertEqual(resp.status_code, 200)
        
    def test_view_url_by_name(self):
        
        resp = self.client.get(reverse('home'))
        
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        
        resp = self.client.get(reverse('home'))
        
        self.assertEqual(resp.status_code, 200)
        
        self.assertTemplateUsed(resp, 'home.html')