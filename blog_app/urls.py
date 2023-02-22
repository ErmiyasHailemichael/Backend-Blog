from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.BlogView.as_view(), name='blog_view'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
]

