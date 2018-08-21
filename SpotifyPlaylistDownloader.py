import spotipy
import sys
from spotipy import util
import json
def editPlaylist(results):
    for i in range(46):
        del results['items'][i]['added_at']
        del results['items'][i]['added_by']
        del results['items'][i]['is_local']
        del results['items'][i]['primary_color']
        del results['items'][i]['track']['album']['available_markets']
        del results['items'][i]['track']['album']['href']
        del results['items'][i]['track']['album']['id']

    file = open("Playlist.json", "w")
    jsonarray = json.dumps(results, indent=4, sort_keys=True)
    file.write(jsonarray)
    file.close
Playlist_ID= input("What is ID? ")
userna
token = util.prompt_for_user_token(username=username,scope="playlist-read-collaborative",client_id="",client_secret=,redirect_uri="https://youtube.c
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.user_playlist_tracks(playlist_id=Playlist_ID,limit=10offset=0,user=username)
    editPlaylist(results)

