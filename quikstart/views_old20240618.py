from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.views import View


def auth(request):
    if request.method == 'GET':
        return JsonResponse({'status': True, 'message': 'GET'})
    elif request.method == 'POST':
        return JsonResponse({'status': True, 'message': 'POST'})
    return JsonResponse({'status': True, 'message': 'success'})


#@api_view(['GET']) # DRF的
# def login(request):
#     return Response({'status': True, 'message': 'success'})


# class InfoView(APIView):
#     def get(self, request):
#         return Response({'status': True, 'message': 'success'})

class UserView(View): # View是Django的基类
    def get(self, request, pk):
        print(request)
        # django的request对象
        # request.GET
        # request.POST
        # request.body
        # request.FILES
        return JsonResponse({'status': True, 'message': 'GET'})
    def post(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'POST'})

    def put(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'PUT'})
    def delete(self, request, *args, **kwargs):
        return JsonResponse({'status': True, 'message': 'DELETE'})

class InfoView(APIView): # APIView继承自Django的View，是DRF的基类
    def get(self, request, dt):
        print(request)
        #drf的request对象，是对django的request对象的又一层封装
        # request._request.GET
        # request._request.POST
        # request._request.method

        # 如果不通过request，想要获取请求中的参数，可以用如下方式，因为在上层的dispatch源码中，将请求中的参数都放到了args和kwargs中
        # self.args
        # self.kwargs
        return Response({'status': True, 'message': 'success'})

    def post(self, request, *args, **kwargs):
        return Response({'status': True, 'message': 'success'})

    def put(self, request):
        return Response({'status': True, 'message': 'success'})

    def delete(self, request):
        return Response({'status': True, 'message': 'success'})
