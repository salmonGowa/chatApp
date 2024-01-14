from django.shortcuts import render

def index(request):
    return render(request,'chat/index.html',{})

def room (request):
    return render(request,'chat/room.html',{
        'room_name_json':mark_safe(json.dumps(room_name))
    })