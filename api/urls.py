from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ProjectViewSet, ProjectMemberViewSet, TaskViewSet, CommentViewSet, LoginView

# Set up the router and register viewsets
router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('projects', ProjectViewSet, basename='project')
router.register('project-members', ProjectMemberViewSet, basename='project-member')
router.register('tasks', TaskViewSet, basename='task')
router.register('comments', CommentViewSet, basename='comment')

# Define URL patterns
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  # Add a login endpoint
    path('', include(router.urls)),  # Include the router's URLs
]
