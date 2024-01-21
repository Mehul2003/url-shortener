from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from urls.models import Path
from urls.serializers import PathSerializer

# Create your views here.

@csrf_exempt
def pathApi(request):
    if request.method == 'GET': # get real url from alt
        if request.GET.get('id') != None:
            id = str(request.GET.get('id'))
            try:
                path = Path.objects.get(alt=id)
            except:
                return JsonResponse("Invalid Id", safe=False)
            path_serializer = PathSerializer(path)
            return JsonResponse(path_serializer.data, safe=False)
        else:
            paths = Path.objects.all()
            path_serializer = PathSerializer(paths, many=True)
            return JsonResponse(path_serializer.data, safe=False)
    elif request.method == 'POST': # create alt url from real
        path_data = JSONParser().parse(request)
        path_serializer = PathSerializer(data=path_data)
        if path_serializer.is_valid():
            path_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    # elif request.method == 'PUT': # modify alt url from real
    #     path_data = JSONParser().parse(request)
    #     path = Path.objects.get(alt=path_data["alt"])
    #     path_serializer = PathSerializer(path, data=path_data)
    #     if path_serializer.is_valid():
    #         path_serializer.save()
    #         return JsonResponse("Update Successfully", safe=False)
    #     return JsonResponse("Failed to update", safe=False)
    # elif request.method == 'DELETE': # delete alt from real
    #     path_data = JSONParser().parse(request)
    #     path = Path.objects.get(endpoint=path_data["alt"])
    #     path.delete()
    #     return JsonResponse("Deleted successfully", safe=False)