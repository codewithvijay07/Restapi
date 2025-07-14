from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from .models import Students
from .serializers import StudentSerializers

class StudentView(APIView):
    
    def get(self, request, *args, **kwargs):
        result = Students.objects.all()
        serializers = StudentSerializers(result, many=True)
        return Response({'status': 'Success', 'student': serializers.data}, status=200)
    
    def post(self, request):
        serializers = StudentSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status': 'Success', 'data': serializers.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'Error', 'errors': serializers.errors}, status=status.HTTP_400_BAD_REQUEST)




# from django.shortcuts import render
# from rest_framework import APIView
# from rest_framework.response import Response 
# from rest_framework import status
# from .models import Students
# from .serializers import StudentSerializers
# # Create your views here.
# class StudentView(APIView):
    
#     def get(self,request,*arg,**kwargs):
#         result=Students.objects.all()
#         serializers=StudentSerializers(result,many=True)
#         return  Response({'status':'Success','student':serializers.data},status=200)
    
#     def post(self,request):
#         serializers=StudentSerializers(data=request.data)
#         if serializers.is_valid():