from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stdinfo/<int:pk>',student_detail,name='student_detail'),
    path('stdinfo/',student_list,name='student_list')
]
