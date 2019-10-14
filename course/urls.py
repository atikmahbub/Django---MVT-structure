from django.urls import path
from .views import ( 
        CourseCreateView,
        CourseListView,
        CourseDetailView,
        CourseUpdateView,
        CourseDeleteView
     )

app_name = 'course'

urlpatterns = [
    path('', CourseListView.as_view(),name='course-list'),
    path('<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('create/', CourseCreateView.as_view(),name='course-create'),
]
