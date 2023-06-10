from django.shortcuts import render
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse
import random
import time
import json
from .models import RoomMember

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def getToken(request):
    appId = 'APP ID'
    appCertificate = 'APP CERTIFICATE'
    channelName = request.GET.get('channel')
    uid = random.randint(1, 250)
    expirationTimeInSeconds = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)


def lobby(request):
    return render(request, 'lobby.html')


def room(request):
    return render(request, 'room.html')


@csrf_exempt
def createUser(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name': data['name']}, safe=False)


def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(uid=uid, room_name=room_name,)

    name = member.name
    return JsonResponse({'name': member.name}, safe=False)


@csrf_exempt
def deleteUser(request):
    data = json.loads(request.body)

    member = RoomMember.objects.get(name=data['name'], uid=data['UID'], room_name=data['room_name'])

    member.delete()

    return JsonResponse('Member deleted', safe=False)
