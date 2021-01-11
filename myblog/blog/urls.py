from django.urls import path, include
from .views import *


urlpatterns = [
    path('', BlogPostListView.as_view()),
    path('category', BlogPostCategoryView.as_view()),
    path('<slug>', BlogPostDetailView.as_view()),
]