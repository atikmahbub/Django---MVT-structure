from django.urls import path
from .views import about_view,contact_view


urlpatterns = [
    path('', about_view , name="About"),
    path('contact/', contact_view , name="Contact"),
]
