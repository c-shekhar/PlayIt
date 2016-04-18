"""CodeEx API views"""

import json
import requests

from flask import request, render_template, jsonify

from pusher import Pusher
app_id, key, secret = '195837', "5130eac739325a024e28", "b9e7abd35cae52415206"
pusher = Pusher(app_id=app_id, key=key, secret=secret)

_SONGS = []
_CLIENT_ID = "98185dd646f78421963744faa9144ffa"

def index():
    return "Hello! World"

def user():
    return render_template('index.html')

def server():
    return render_template('player.html')

def push():
    track_id = request.form['trackId']
    print(track_id)
    # song_url = get_song_url(track_id)
    song_url = track_id.replace('I','')
    _SONGS.append(song_url)

    pusher.trigger('notifications', 'new_notification', {'songs': _SONGS})  
    return jsonify({"songs": _SONGS})

# def get_song_url(track_id):
#     # url = "http://api.soundcloud.com/tracks/{}?client_id={}"
#     # url = url.format(track_id.replace('I',''), _CLIENT_ID)
#     # song_meta = requests.get(url).json()
#     # print song_meta
#     # stream_url = song_meta['stream_url']
#     return track_id.replace('I','')

def list():
    return {'songs': _SONGS}


"""
possible additions:
    download current track
    no result? add local version of song
"""