from django.shortcuts import redirect
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer

tags = [["companies"], ["advocates"]]


class APIHomeView(APIView):
    def get(self, request):
        data = ["Advocate:/"]
        return Response(data)


class CompaniesListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get companies list",
        description="""
            This endpoint retreives all companies in our db".
        """,
        tags=tags[0],
    )
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)


class CompanyDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get companies by name",
        description="""
            This endpoint retreives a company's detail using its name".
        """,
        tags=tags[0],
    )
    def get(self, request, name):
        company = Company.objects.get(name=name)
        serializer = CompanySerializer(company, context={"request": request})

        return Response(serializer.data)


class AdvocatesListView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get advocates list",
        description="""
            This endpoint retreives all advocates in our db".
        """,
        tags=tags[1],
    )
    def get(self, request):
        query = request.GET.get("query")
        if query == None:
            query = ""
        advocates = Advocate.objects.filter(
            Q(name__icontains=query) | Q(bio__icontains=query)
        )
        serializer = AdvocateSerializer(advocates, many=True)

        return Response(serializer.data)

    @extend_schema(
        summary="Create an advocate",
        description="""
            This endpoint creates an advocate".
        """,
        tags=tags[1],
    )
    def post(self, request):
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class AdvocateDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get advocates detail",
        description="""
            This endpoint retreives an advocate's detail using id".
        """,
        tags=tags[1],
    )
    def get(self, request, id):
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocateSerializer(advocate, context={"request": request})

        return Response(serializer.data)

    @extend_schema(
        summary="Update advocate",
        description="""
            This endpoint updates advocate detail".
        """,
        tags=tags[1],
    )
    def put(self, request, id):
        advocate = Advocate.objects.get(id=id)
        serializer = AdvocateSerializer(advocate, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    @extend_schema(
        summary="Delete an advocate",
        description="""
            This endpoint deletes an advocate from our db".
        """,
        tags=tags[1],
    )
    def delete(self, request, id):
        advocate = Advocate.objects.get(id=id)
        advocate.delete()

        return Response({"Status": "Deleted"})
