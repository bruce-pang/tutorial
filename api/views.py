from django.shortcuts import render
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.parsers import JSONParser, FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.versioning import QueryParameterVersioning


class HomeView(APIView):
    # 关于版本
    # 配置文件 VERSION_PARAM = "version" (如果不配置，默认为version)
    # http://127.0.0.1:8000/home/?version=v1 -> request.version = v1
    # versioning_class = QueryParameterVersioning

    # 关于解析器

    # parser_classes = api_settings.DEFAULT_PARSER_CLASSES # 所有的解析器
    # content_negotiation_class = api_settings.DEFAULT_CONTENT_NEGOTIATION_CLASS # 根据请求头， 匹配解析器
    parser_classes = [JSONParser, FormParser, MultiPartParser]
    content_negotiation_class = DefaultContentNegotiation
    def get(self, request, *args, **kwargs):
        print(request.version)
        return Response("....")
    def post(self, request, *args, **kwargs):
        print(request.data, type(request.data))
        return Response("OK")
