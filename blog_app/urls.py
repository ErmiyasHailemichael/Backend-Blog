from django.urls import path
from . import views
from .views import BlogList , BlogDetail

urlpatterns = [
    # path('', views.index, name='index'),
    path('', Blog.as_view(), name='blog'),
    path('<int:pk>/', BlogDetail.as_view(), name='blog_detail'),
]

