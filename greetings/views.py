from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from greetings.models import Mobiles
from greetings.serializers import GreetingsSerializers

# Create your views here
class GreetingsView(APIView):
    def get(self,request,*args,**kw):
        qs=Mobiles.objects.all()
        serializer=GreetingsSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kw):
        serializer=GreetingsSerializers(data=request.data)
    
        return Response(data="mobile created")    