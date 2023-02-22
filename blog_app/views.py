from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.view import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Blog
from .serializers import BlogSerializer
from django.shortcuts import get_object_or_404


# Create your views here.

# class /iblog (blog)
# GET/iblog -index
# Post/iblog -create

# class /iblog/:id(BlogDetails)
# GET/iblog/:id -show
# PUT/iblog/:id -update
# DELETE/iblog/:id -delete

class Blog(APIView):

  def get(self, request):
    print(request)
    Blog = Blog.objects.all()
    data = BlogSerializer(blogs, many=True).data
    return Response(data)

    def post(self, request):
      print(request.data)
      data = BlogSerializer(data=request.data)
      if Blog.is_valid():
        Blog.save()
        return Response(Blog.data, status=status.HTTP_201_CREATED)
      else:
        return Response(Blog.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetail(APIView):

    #Show
    def get(self, request, pk):
      blog = get_object_or_404(Blog, pk=pk)
      data = BlogSerializer(blog).data
      return Response(data)
  
    #Update
    def put(self, request, pk):
      
      blog = get_object_or_404(Blog, pk=pk)
      updated_blog = BlogSerializer(blog, data=request.data)
      if updated_blog.is_valid():
        updated_blog.save()
        return Response(updated_blog.data)
      else:
        return Response(updated_blog.errors, status=status.HTTP_400_BAD_REQUEST)
  #Delete
    def delete(self, request, pk):
      blog = get_object_or_404(Blog, pk=pk)
      blog.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)




def index(request):
  return HttpResponse('<h1> Welcome to our campus! </h1>')