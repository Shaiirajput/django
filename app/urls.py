from django.urls import path,include
from . import views
#........... for modelviewset..............
from rest_framework import routers
router=routers.DefaultRouter()
router.register('sapi',views.StudentModelViewSet,basename="student")
urlpatterns = [
    path('', include(router.urls)),
    
    #........Function based api..........
    path('student/',views.hello_world),
    path('studentapi/',views.student_api),
    path('studentapi/<int:pk>',views.student_api),

    #.......class based api...........
    path('stuapi/',views.StudentAPI.as_view()),
    path('stuapi/<int:pk>/',views.StudentAPI.as_view()),

    #..........generic APIView and mixin crud.........
    path('stustudent/',views.LCStudentAPI.as_view()),
    #path('c/',views.StudentCreate.as_view()),
    #path('stustudent/<int:pk>/',views.StudentRetrieve.as_view()),
    #path('stustudent/<int:pk>/',views.StudentUpdate.as_view()),
    path('stustudent/<int:pk>/',views.RUDStudentAPI.as_view()),
    
    #...........concrete view class...........
    path('api/',views.StudentList.as_view()),
    #path('apic/',views.StudentCreate.as_view()),
    #path('api/<int:pk>/', views.StudentRetreive.as_view()),
    #path('api/<int:pk>/', views.StudentUpdate.as_view()),
    #path('api/<int:pk>/', views.StudentDestroy.as_view()),
    path('api/<int:pk>/',views.StudentRetUpdDes.as_view() ),

    path('resumeapi/',views.ResumeAPI.as_view()),
    
    
    
]

