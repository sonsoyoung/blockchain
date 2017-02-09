from django.shortcuts import render
from django.utils import timezone
from .models import Post
import json
import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer

from django.http import JsonResponse
from django.http import HttpResponse
from .models import Book

import sqlite3
def post_list(request):
	url = 'http://127.0.0.1:7050/registrar'
	payload = {
	  "enrollId": "admin",
      "enrollSecret": "Xurw3yU9zI0l"
	}
	headers = {'content-type': 'application/json'}
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	json_load = json.loads(r.text)
	#
	#
	# test = {
	# 	"name" : 'soyoung',
	# 	"age": json_load['age'],
	# }

	#return render(request, 'blog/post_list.html', {})
	return JsonResponse(json_load)

def chaincode(request):
		url = 'http://127.0.0.1:7050/chaincode'
		payload = {
		  "jsonrpc": "2.0",
		  "method": "deploy",
		  "params": {
		    "type": 1,
		    "chaincodeID":{
		        "name": "mycc"
		    },
		    "input": {
		        "args":["init", "a", "100", "b", "200"]
		    }
		  },
		  "id": 1
		}

		headers = {'content-type': 'application/json'}
		r = requests.post(url, data=json.dumps(payload), headers=headers)
		json_load = json.loads(r.text)

		return JsonResponse(json_load)

def animal(request):
	return render(request, 'blog/animal.py', {})

def test(request):
	return render(request, 'blog/test.html', {})



def test2(request):
	return render(request, 'blog/script2.js', {})




class UserViewSet(viewsets.ModelViewSet):
    """
    사용자(user)를 보거나 편집하는 API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    그룹(group)을 보거나 편집하는 API
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
