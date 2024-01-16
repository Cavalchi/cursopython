# funcoes.py
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def play_pause_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='f31f836299394c619b9a089f73ada300',
                                                   client_secret='955ad2963f444c2d9ac40a46f271f690',
                                                   redirect_uri='http://localhost:8888/callback',
                                                   scope='user-modify-playback-state user-read-playback-state'))
    playback_info = sp.current_playback()
    if playback_info is not None and playback_info['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def next_track_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='f31f836299394c619b9a089f73ada300',
                                                   client_secret='955ad2963f444c2d9ac40a46f271f690',
                                                   redirect_uri='http://localhost:8888/callback',
                                                   scope='user-modify-playback-state user-read-playback-state'))
    sp.next_track()
