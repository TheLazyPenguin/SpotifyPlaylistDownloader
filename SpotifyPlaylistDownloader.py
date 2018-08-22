import spotipy
import sys
from spotipy import util
import json
import config as cg
Track_name=[]
Artist_name=[]
Album_name=[]
Image_links=[]
Release_date=[]
def editPlaylist(results):
    for i in range(46):
        Album_name.append(results['items'][i]['track']['album']['name'])
        Artist_name.append(results['items'][i]['track']['album']['artists'][0]['name'])
        Track_name.append(results['items'][i]['track']['name'])
        Image_links.append(results['items'][i]['track']['album']['images'][0]['url'])
        Release_date.append(results['items'][i]['track']['album']['release_date'])



    file = open("Playlist.json", "w")
    jsonarray = json.dumps(results, indent=4, sort_keys=True)
    file.write(jsonarray)
    file.close
Playlist_ID= input("What is ID? ")
token = util.prompt_for_user_token(username=cg.username,scope="playlist-read-collaborative",client_id=cg.client_id,client_secret=cg.client_secret,redirect_uri=cg.redirect_uri)
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.user_playlist_tracks(playlist_id=Playlist_ID,limit=100,offset=0,user=cg.username)
    editPlaylist(results)

