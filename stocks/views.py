from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from stocks.crawler import StockCrawler
from stocks.serializer import IPOSerializer


class Run(APIView):
    def get(self, request, *args, **kwargs):
        s = StockCrawler()
        result = s.get_list()
        serializer = IPOSerializer(result, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
