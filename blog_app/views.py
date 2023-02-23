from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
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

class BlogView(APIView):
  #Index-Get
  def get(self, request):
    print(request)
    blog = Blog.objects.all()
    data = BlogSerializer(blog, many=True).data
    return Response(data)

  #Post -works in postman
  def post(self, request):
    print(request.data)
    blog = BlogSerializer(data=request.data)
    if blog.is_valid():
      blog.save()
      return Response(blog.data, status=status.HTTP_201_CREATED)
    else:   
      return Response(blog.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetail(APIView):

    #Show - works in postman
    def get(self, request, pk):
      blog = get_object_or_404(Blog, pk=pk)
      data = BlogSerializer(blog).data
      return Response(data)
  
    #Update - works in postman 
    def put(self, request, pk):
      print(request)
      blog = get_object_or_404(Blog, pk=pk)
      updated_blog = BlogSerializer(blog, data=request.data)
      if updated_blog.is_valid():
        updated_blog.save()
        return Response(updated_blog.data)
      else:
        return Response(updated_blog.errors, status=status.HTTP_400_BAD_REQUEST)

  #Delete - works in postman
    def delete(self, request, pk):
      blog = get_object_or_404(Blog, pk=pk)
      blog.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)




def index(request):
  return HttpResponse('<h1> Welcome to our campus! </h1>')