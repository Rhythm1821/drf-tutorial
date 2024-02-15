from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

# Create your views here.
@api_view(['GET','POST'])
def snippet_list(request, format=None):
    """
    List all code snippets or create a new snippet
    """
    if request.method=='GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)
    
    if request.method=='GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=404)
    
    elif request.method=='DELETE':
        snippet.delete()
        return HttpResponse(status=204)