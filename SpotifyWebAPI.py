import spotipy
import webbrowser
import json
Track_name=[]
Artist_name=[]
Album_name=[]
Image_links=[]
Release_date=[]
Track_length=[]
def editPlaylist(results):
    num = results['total']
    for i in range(num):
        Album_name.append(results['items'][i]['track']['album']['name'])
        Artist_name.append(results['items'][i]['track']['album']['artists'][0]['name'])
        Track_name.append(results['items'][i]['track']['name'])
        Image_links.append(results['items'][i]['track']['album']['images'][0]['url'])
        Release_date.append(results['items'][i]['track']['album']['release_date'])
        Track_length.append(results['items'][i]['track']['duration_ms'])
    return num


    file = open("Playlist.json", "w")
    jsonarray = json.dumps(results, indent=4, sort_keys=True)
    file.write(jsonarray)
    file.close
Playlist_ID= input("What is Playlist ID? ")
webbrowser.open("https://accounts.spotify.com/authorize?client_id=eaa2b856a56a495699ac28193ea694fa&redirect_uri=https://localhost&scope=playlist-read-collaborative&response_type=token&state=123")
token = input("Paste link shown after logging in ")
username = input("Input Spotify Username")
token,foo,floo,fla = token.split("&")
foo,token = token.split("=")
del foo,floo,fla
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.user_playlist_tracks(playlist_id=Playlist_ID,limit=100,offset=0,user=username)
    num = editPlaylist(results)

