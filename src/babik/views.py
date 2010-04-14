import mpdclient2
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponsePermanentRedirect
from django.conf import settings

def get_track_time(time_status):
        time_list = time_status.split(':')
        time_position = divmod(int(time_list[0]), 60)
        time_end = divmod(int(time_list[1]), 60)
        time = {'position': time_position,
                'end': time_end,
                }
        return time

def index(request):
    return HttpResponseRedirect('/playlist')

def playlist(request):
    context = {'next': request.path,
               'page': "playlist",
               'media_url': settings.MEDIA_URL,
               }
    try:
        m = mpdclient2.connect()
    except socket.error:
        m = False

    if m:
        playlistinfo = m.playlistinfo()
        currentsong = m.currentsong()
        status = m.status()
        if hasattr(currentsong, 'artist') and hasattr(status, 'time'):
            time = get_track_time(status.time) 
            context['time'] = time
            context['currentsong'] = currentsong

        context['playlist'] = playlistinfo
        context['status'] = status

    else:
        context = {'errors': ['could not connect to server']}

    return render_to_response('babik/playlist.html', context)

def browse(request, path):
    context = {'next': request.path,
               'page': "browse",
               'media_url': settings.MEDIA_URL,
               }

    try:
        m = mpdclient2.connect()
    except socket.error:
        m = False

    if m:
        playlistinfo = m.playlistinfo()
        if not path:
            list = m.lsinfo()
        else:
            list = m.lsinfo(path)

        currentsong = m.currentsong()
        status = m.status()
        if currentsong and hasattr(status, 'time'):
            time = get_track_time(status.time) 
            context['time'] = time

        context['list'] = list
        context['currentsong'] = currentsong
        context['status'] = status
        context['playlist'] = playlistinfo
    else:
        context = {'errors': ['could not connect to server']}

    return render_to_response('babik/browse.html', context)

def controller(request, action, songid=None):
    context = {}
    next = False

    try:
        m = mpdclient2.connect()
    except socket.error:
        m = False

    if m:
        if action == "next":
            m.next()
        elif action == "pause":
            m.pause()
        elif action == "play":
            m.play()
        elif action == "stop":
            m.stop()
        elif action == "previous":
            m.previous()
        elif action == "add" and request.POST and request.POST.has_key('path'):
            m.add(request.POST['path'])
        elif action == "clear":
            m.clear()
        elif action == "replace":
            m.clear()
            m.add(request.POST['path'])
            m.play()
        elif action == "deleteid" and songid:
            m.deleteid(int(songid))
        elif action == "playid" and songid:
            m.playid(int(songid))
        elif action == "volume_up":
            status = m.status()
            volume = int(status.volume)
            volume_new = volume + 5
            m.setvol(volume_new)
        elif action == "volume_down":
            status = m.status()
            volume = int(status.volume)
            volume_new = volume - 5
            m.setvol(volume_new)

        if request.POST and request.POST.has_key('next'):
            next= request.POST['next']
            return HttpResponseRedirect(next)

    return HttpResponseRedirect('/playlist/')
