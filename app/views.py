from django.shortcuts import render
from rest_framework.decorators import api_view#....FOR FUNCTION BASED VIEW.....
from rest_framework.response import Response
from .models import Student,Resume
from .serializers import StudentSerializer,ResumeSerializer
from rest_framework import status
from rest_framework .views import APIView#......for class based view....
#...........FOR GenericAPIView and Model Mixin........................
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
#.............concrete view API.......................
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,RetrieveUpdateDestroyAPIView
#............for modelViewSET ...................
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated 

# Create your views here.
#................function based view...................
@api_view(['POST'])
def hello_world(request):
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'I WANT TO CHECK THE REQUEST YES this is a post request','data':request.data})
    return Response({'msg':'hello world'})
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):
    if request.method=='GET':
        id=pk
        #id=request.data.get('id')
        if id is not None:
            #....creating model instance(object)....
            stu=Student.objects.get(id=id)
            #....converting into python dict/serializing object....
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        #.....queryset......
        stu=Student.objects.all()
        #.....converting  queryset to list of pythonobject dict/serilizing queryset...
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)    
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PUT':
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated successfully!!'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='PATCH':
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partially  Data Updated successfully!!' },status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted successfully!!'},status=status.HTTP_410_GONE)
    
#....for class based API...........
class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        #id=request.data.get('id')
        if id is not None:
            #....creating model instance(object)....
            stu=Student.objects.get(id=id)
            #....converting into python dict/serializing object....
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        #.....queryset......
        stu=Student.objects.all()
        #.....converting  queryset to list of pythonobject dict/serilizing queryset...
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk,format=None):
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated successfully!!'},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request,pk,format=None):
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partially  Data Updated successfully!!' },status=status.HTTP_206_PARTIAL_CONTENT)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        id=pk
        #id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted successfully!!'},status=status.HTTP_410_GONE)
#.........generic APIVIEW and mixins. CRUD..............

    #.....list and create -dont use pk
class LCStudentAPI(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):                                                                                                      
        return self.create(request,*args,**kwargs)

#.................retrieve ,update and destroy.  Pk required.................  
class RUDStudentAPI(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    
#..........................Concrete ApiView....................................................
class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetreive(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset= Student.objects.all()
    serializer_class=StudentSerializer
class StudentRetUpdDes(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
#...................MODELVIEWSET........................
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #authentication_classes=[BasicAuthentication]
    #permission_classes=[IsAuthenticated]


class ResumeAPI(APIView):
      def post(self,request,format=None):
        serializer=ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created Successfully!!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
      def get(self,request,pk=None,format=None):
        id=pk
        #id=request.data.get('id')
        if id is not None:
            #....creating model instance(object)....
            stu=Resume.objects.get(id=id)
            #....converting into python dict/serializing object....
            serializer=ResumeSerializer(stu)
            return Response(serializer.data)
        #.....queryset......
        stu=Resume.objects.all()
        #.....converting  queryset to list of pythonobject dict/serilizing queryset...
        serializer=ResumeSerializer(stu,many=True)
        return Response(serializer.data)





    
    



 
    