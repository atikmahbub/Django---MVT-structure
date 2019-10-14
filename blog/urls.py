from django.urls import path

from .views import ( 
        BlogCreateView,
        BlogView,
        BlogDetailView,
        BlogUpdateView,
        BlogDeleteView
     )

app_name = 'blog'
urlpatterns = [
    path('', BlogView.as_view(),name='blog-list'),
    path('<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('<int:id>/delete/', BlogDeleteView.as_view(), name='blog-delete'),
    path('<int:id>/update/', BlogUpdateView.as_view(), name='blog-update'),
    path('create/', BlogCreateView.as_view() ,name='blog-create'),
]
