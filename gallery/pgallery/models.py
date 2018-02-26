from django.db import models


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=60)

    def __str__:
        return self.name

class Image(model.Models):
    image=models.ImageField(upload_to='gallery/', blank=True)
    image_link=models.TextField(blank=True)
    image_name=models.TextField(max_length=60 , blank=True)
    details=models.TextField(max_length=60, blank=60)
    pub_date = models.DateTimeField(auto_now_add=True)
    category=models.ManytoManyField(category)
    location = models.ManytoManyField(location)

    def __str__:
        return self.image

