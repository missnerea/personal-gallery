from django.test import TestCase
from .models import Category,Location,Image

# Create your tests here.
class ImageTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.image=Image(image_name='twins' details='cute twins')

        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))