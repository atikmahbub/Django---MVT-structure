from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    active = models.BooleanField(default= True)
    image = models.ImageField(upload_to= 'blog_image/' , null=True , blank=True)

    def get_absolute_url(self):
        return reverse("blog:blog-detail", kwargs= {"id": self.id})
