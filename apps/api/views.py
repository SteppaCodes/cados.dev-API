from django.shortcuts import redirect

from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q

from . models import Advocate 
from .serializers import AdvocateSerializer


class APIHomeView(APIView):
    def get(self, request):
        data = ["Advocate:/"]
        return Response(data)
    

class AdvocatesListView(APIView):
    def get(self, request):
        query = request.GET.get("query")
        if query == None:
            query = ''
        advocates = Advocate.objects.filter(Q(name__icontains=query)
                                            | Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        

class AdvocateDetailView(APIView):
    def get(self, request, id):
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocateSerializer(advocate)

        return Response(serializer.data)
    
    def put(self, request, id):
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocateSerializer(advocate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, id):
        advocate = Advocate.objects.get(id=id)
        advocate.delete()

        return Response({
            "Status":"Deleted"
        })
