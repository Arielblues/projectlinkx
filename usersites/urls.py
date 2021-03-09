from django.urls import path
from .views import (
    xPostListView,
    xPostDetailView,
    xPostCreateView,
    xPostUpdateView,
    xPostDeleteView,
    xUserPostListView,
    SitecategoryCreateView,
    SitecategoryDetailView
)
from . import views

urlpatterns = [
    path('', xPostListView.as_view(), name='xblog-home'),
    path('myurls', views.xhomeuser, name='xblog-homeuser'),
    path('user/<str:username>', xUserPostListView.as_view(), name='uxser-posts'),
    path('url/<int:pk>/', xPostDetailView.as_view(), name='xpost-detail'),
    path('url/new/', xPostCreateView.as_view(), name='xpost-create'),
    path('url/<int:pk>/update/', xPostUpdateView.as_view(), name='xpost-update'),
    path('url/<int:pk>/delete/', xPostDeleteView.as_view(), name='xpost-delete'),
    path('category/new/', SitecategoryCreateView.as_view(), name='xxpost-create'),
    path('category/<int:pk>/', SitecategoryDetailView.as_view(), name='xxpost-detail'),
    path('mycategories', views.xxhomeuser, name='xxblog-homeuser'),
    path('create/', views.BookCreateView.as_view(), name='create_book'),
]
