from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import *
from .serializer import *
@api_view(['GET','POST'])
def suggestions(request):
    if request.method == "GET":
        suggestions = SuggestionsData.objects.all().order_by("-vote")
        #    print(suggestions)
        serialize = SuggestionsDataSerializer(suggestions,many = True)
        #    print(serialize.data)
        return Response(serialize.data) 
    elif request.method == "POST":
        print(request.data)
        serialize = SuggestionsDataSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({
                "data":serialize.data
            })
@api_view(['GET'])
def vote(request,id):
   
    try:
        data = SuggestionsData.objects.get(id = int(id))
        data.vote +=1
        data.save()
        serialize = SuggestionsDataSerializer(data)
        return Response(serialize.data)
    except Exception as e:
        return Response({"Error" :str(e)})



