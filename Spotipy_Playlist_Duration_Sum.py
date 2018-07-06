import serial
import time
import urllib
import spotipy
import spotipy.util as util
import os

scope = 'user-read-currently-playing'
print("Please enter your username")
username = raw_input()
print("Please enter the given playlist ID")
playlist_id = raw_input()
print("Please enter your client ID")
client_id = raw_input()
print("Please enter your client secret")
client_secret = raw_input()
print("Please enter your redirect url")
redirect_url = raw_input()
token = util.prompt_for_user_token(username,scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_url)
spotify = spotipy.Spotify(auth=token)
playlist = spotify.user_playlist(username, playlist_id=playlist_id)
playlist_tracks = playlist['tracks']['items'] 
track_duration = []
for track in playlist_tracks:
    track_duration.append(float(track['track']['duration_ms']))
print(sum(track_duration) / 100 / 60 / 60)