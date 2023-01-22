from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Movies
from api.serializers import MovieSerializer,MovieModelSerializer,UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import authentication,permissions
from django.contrib.auth.models import User
# class MovieView(APIView):
#     def get(self,request,*args,**kwargs):
#         qs=Movies.objects.all()
#         serializer=MovieSerializer(qs,many=True)
#         return Response(data=Serializer.data)
#     def post(self,request,*args,**kwargs):
#         serializer=MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             Movies.objects.create(**serializer.validated_data)
#             return Response(data=serializer.data)
#         else:
#             return Response(data=serializer.errors)
# class MovieDetailView(APIView):
#     def get(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Movies.objects.get(id=id)
#         serializer=MovieSerializer(qs,many=False)
#         return Response(data=serializer.data)
#     def put(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         Movies.objects.get(id=id).update(**request.data)
#         qs=Movies.objects.get(id=id)
#         serializer=MovieSerializer(qs,many=False)
#         return Response(data=serializer.data)
#     def delete(self,request,*args,**kwargs):
#         id=kwargs.get("pk")
#         qs=Movies.objects.get(id=id).delete()
#         return Response(data="deleted")
class MovieViewSetView(viewsets.ModelViewSet):
    serializer_class = MovieModelSerializer
    queryset = Movies.objects.all()
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # def list(self,request,*args,**kwargs):
    #     qs=Movies.objects.all()
    #     serializer=MovieModelSerializer(qs,many=True)
    #     return Response(data=serializer.data)
    # def create(self,request,*args,**kwargs):
    #     serializer=MovieModelSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    # def retrieve(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     qs=Movies.objects.get(id=id)
    #     serializer=MovieModelSerializer(qs,many=False)
    #     return Response(data=serializer.data)
    # def destroy(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     Movies.objects.get(id=id).delete()
    #     return Response(data="deleted")
    # def update(self,request,*args,**kwargs):
    #     id=kwargs.get("pk")
    #     obj=Movies.objects.get(id=id)
    #     serializer=MovieModelSerializer(data=request.data,instance=obj)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)
    @action(methods=["GET"],detail=False)
    def genres(self,request,*args,**kwargs):
        res=Movies.objects.values_list("genre",flat=True).distinct()
        return Response(data=res)
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # def create(self,request,*args,**kwargs):
    #     serializer=UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)











