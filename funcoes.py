# funcoes.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_pause_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='seu-client-id',
                                                   client_secret='seu-client-secret',
                                                   redirect_uri='http://localhost:8888/callback',
                                                   scope='user-modify-playback-state'))
    playback_info = sp.current_playback()
    if playback_info['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()
