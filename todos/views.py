# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
#from rest_framework.renderers import TemplateHTMLRenderer
#from rest_framework.response import Response
#from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView
from .serializers import TodoSerializer

# Create your views here.
def index(request):
    todos = Todo.objects.all()[:10]
    context ={
        'todos':todos
    }
    return render(request,'index.html',context)

def details(request, id):
    todo = Todo.objects.get(id=id)
    context ={
        'todo':todo
    }
    return render(request,'details.html',context)

def add(request):
    if(request.method =='POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title=title,text=text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request,'add.html')

def delete(request,id):
    Todo.objects.filter(id=id).delete()
    

    return redirect('/todos')
'''
class TodoDeleteAPIView(DestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field ='id'
 '''   
        
'''
class index_1(APIView):
    renderer_class = [TemplateHTMLRenderer]
    template_name = 'index.html'
    def get(self,request):
        queryset = Todo.objects.all()
        return Response({'todos':queryset})
'''