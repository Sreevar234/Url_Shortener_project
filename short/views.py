from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import short_url
from .serializer import short_url_serializer,update_url_serializer,basic_serializer
from rest_framework import status
from django.shortcuts import redirect
# Create your views here.


class create_short_url(APIView):
    def post(self,request):
        data=request.data
        s=short_url_serializer(data=data)
        s.is_valid(raise_exception=True)
        data_check=s.validated_data["long_url"]
        data_exsist=short_url.objects.filter(long_url=data_check).first()
        if data_exsist:
            serializer=basic_serializer(data_exsist)
            return Response(
                    serializer.data,
    
            )
        else:
            data_object=s.save()#s.save() returns the data object created
            serializer=basic_serializer(data_object)
            return Response(
                serializer.data,
            )
    

class update_short_url(APIView):
    def put(self,request,short_code):
        link=short_url.objects.get(short_code=short_code)
        serializer=update_url_serializer(instance=link,data=request.data)
        serializer.is_valid()
        serializer.save()
        data=serializer.data
        return Response(
            data
        )
    

class delete_short_url(APIView):
    def delete(self,request,short_code):
        link=short_url.objects.get(short_code=short_code)
        link.delete()
        return Response("data deleted")
    
    
class get_long_url(APIView):
    def get(self,request,short_code):
        link=short_url.objects.get(short_code=short_code)
        serializer=short_url_serializer(link)
        data=serializer.data
        return Response(
            data
        )


class redirect_url(APIView):
    def get(self,request,short_code):
        link=short_url.objects.get(short_code=short_code)
        return redirect(link.long_url)

     