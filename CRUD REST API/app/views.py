from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import QuoteModel
from app.serializers import quoteSerializer

# Create your views here.
class quoteList(APIView):
    def get(self, request):
        xyz = QuoteModel.objects.all()
        serializer = quoteSerializer(xyz, many = True)
        return Response(serializer.data)
    
class quotepost(APIView):
    def post(self,request):
        serializer_data = quoteSerializer(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_data,status=status.HTTP_400_BAD_REQUEST)
         
class quoteUpdate(APIView):
    def get(self, request,pk):
        xyz = QuoteModel.objects.filter(id=pk)
        serializer = quoteSerializer(xyz, many = True)
        return Response(serializer.data)

    def put(self,request,pk):
        existing_data = QuoteModel.objects.get(id=pk)
        d = request.data
        serializer_data = quoteSerializer(existing_data,data=d)
        if serializer_data.is_valid():
            serializer_data.save()
            content = {'message':'data inserted'}
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
class quoteDelete(APIView):
    def delete(self,request,pk):
        to_delete = QuoteModel.objects.filter(id=pk)       
        a = to_delete.delete()
        content = {'message':'data deleted'}
        return Response(content,status=status.HTTP_200_OK)



