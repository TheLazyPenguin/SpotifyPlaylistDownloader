import requests
import urllib
import base64
PlaylistID = input("Input Playlist ID: ")
encode= base64.b64encode(b'eaa2b856a56a495699ac28193ea694fa:447d8103980f40e4a0d21497b6d2bd70')
client_id=b'eaa2b856a56a495699ac28193ea694fa'
client_secret=b'447d8103980f40e4a0d21497b6d2bd70'
header = {'Authorization': "Basic " + str(encode)}
print(header)
dt= {b'grant_type=authorization_code&code=sH4wMnBKq_kJB_6KGyrJ39aojH0MiYLaBIbHQaW_QWFMp7Mwq-F_VsXSEb1Nj9l3zKf9BPQ7yO5JpkMpVxi146WUsejn86hkZpZelC-uQrx0S8tPBYFA9jYh29g&redirect_uri=https://youtube.com&client_id=eaa2b856a56a495699ac28193ea694fa&client_secret=447d8103980f40e4a0d21497b6d2bd70'}
spotifyAPI = requests.post("https://accounts.spotify.com/api/token",data=dt,headers=header)
response = requests.get("https://api.spotify.com/v1/playlists/" + PlaylistID + "/tracks")
print(spotifyAPI.status_code)
print(spotifyAPI.content.decode())