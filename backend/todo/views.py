from django.shortcuts import render
from django.http import HttpResponse
from .models import TaskModel
from .serializer import Taskserializer
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

# TaskModel.objects.create(title = 'apple',desc='fruit')
@csrf_exempt
def tasks(request):
    if request.method == 'GET':

        model_instance = TaskModel.objects.all()
        # print(type(model_instance))
        ser_py = Taskserializer(model_instance,many=True)
        # print(ser_py)
        py_data = ser_py.data
        json_data = JSONRenderer().render(py_data)

        #print(json_data)
        #print(type(json_data))

        return HttpResponse(json_data)

    if request.method == 'POST':
        req_data = request.body
        stream_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(stream_data)
        de_ser = Taskserializer(data = py_data)
        if de_ser.is_valid():
            de_ser.save()
            json_data=JSONRenderer().render({'data':'Data is created'})
            return HttpResponse(json_data)

@csrf_exempt
def task(request,pk):
    model_instance = TaskModel.objects.get(id=pk)
    if request.method == 'GET':
        ser_py = Taskserializer(model_instance)
        py_data = ser_py.data
        json_data = JSONRenderer().render(py_data)
        print(json_data)
        return HttpResponse(json_data)
    
    if request.method == 'PUT':
        req_data = request.body
        strem_data = io.BytesIO(req_data)
        py_data = JSONParser().parse(strem_data)
        de_ser = Taskserializer(model_instance,data = py_data)

        if de_ser.is_valid():
            de_ser.save()
            json_data = JSONRenderer().render({'data':'Data is updated'})
            
        return HttpResponse(json_data)
    

    if request.method == 'DELETE':
        model_instance.delete()
        json_data =JSONRenderer().render({'data':'Data is deleted'})
        return HttpResponse(json_data)
