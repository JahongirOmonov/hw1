from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import NewsSerializer
from rest_framework.response import Response
from .models import NewsModel
from django.shortcuts import get_object_or_404


# Create your views here.

class CreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 2:
                serialzier = NewsSerializer(data=request.data)
                if serialzier.is_valid():
                    serialzier.save()
                    return Response(serialzier.data)
                return Response(serialzier.errors)
        return Response({"msg":"only staff members can add"})
    

class ListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # print(self.request.user)
        # print(request.user, type(request.user), str(request.user))
        # print(request.user.roles, type(request.user.roles))
        if str(request.user) != "AnonymousUser":
            print(self.request.user.roles)
            x = NewsModel.objects.filter(status=True)
            serializer=NewsSerializer(x, many=True)
            return Response(serializer.data)
        return Response({'msg':'Please log in'})
    
class UpdateStatus(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 3:
                x= get_object_or_404(NewsModel, id=kwargs['forid'])
                serializer=NewsSerializer(x, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        return Response("Only admin can change")