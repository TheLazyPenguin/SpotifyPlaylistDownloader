import spotipy
import sys
from spotipy import util

Playlist_ID= input("What is ID? ")
username="lazywolf49@outlook.com"
token = util.prompt_for_user_token(username=username,scope="playlist-read-collaborative",client_id="eaa2b856a56a495699ac28193ea694fa",client_secret="447d8103980f40e4a0d21497b6d2bd70",redirect_uri="https://youtube.com")
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.user_playlist_tracks(playlist_id=Playlist_ID,limit=100,offset=0,user=username)
file = open("Playlist.json","w")
file.write(str(results))
file.close