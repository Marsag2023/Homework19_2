from django.urls import path

from blogpost.apps import BlogPostConfig
from blogpost.views import (BlogPostCreateView, BlogPostDetailView, BlogPostListView,
                            BlogPostUpdateView, BlogPostDeleteView, toggle_activity)

app_name = BlogPostConfig.name

urlpatterns = [
    path('create/', BlogPostCreateView.as_view(), name='create'),
    path('', BlogPostListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogPostDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogPostUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete'),
    path('activity/<int:pk>/', toggle_activity, name="toggle_activity"),
]
