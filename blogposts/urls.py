

from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDeleteView,
    BlogPostDetialView,
    BlogPostUpdateView,
    BlogPostCreateView,
    BlogPostCommentView
    
)

urlpatterns = [
    path('', BlogPostListView.as_view(), name='blogpost_list'),
    path('<int:pk>/edit/', BlogPostUpdateView.as_view(), name='blogpost_edit'),
    path('<int:pk>/', BlogPostCommentView.as_view(), name='blogpost_detail'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
    path('new/', BlogPostCreateView.as_view(), name='blogpost_new'),
]
