from django.db import models
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    image  = models.ImageField(upload_to='course_image/' , blank=True , null = True)

    def get_absolute_url(self):
        return reverse ('course:course-detail' , kwargs={'id' : self.id})