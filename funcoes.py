from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Carrega as variáveis de ambiente
load_dotenv()

# Obtém as variáveis de ambiente
client_id = os.getenv('SPOTIFY_CLIENTE_API')
client_secret = os.getenv('CLIENTE_SECRET_SPOTIFY_API')
redirect_uri = os.getenv('REDIRECT_URI')

# Inicializa o objeto Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='user-modify-playback-state user-read-playback-state'))


def play_pause_spotify():
    playback_info = sp.current_playback()
    if playback_info is not None and playback_info['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def next_track_spotify():
    sp.next_track()

def aumentar_volume_spotify():
    current_volume = sp.current_playback()['device']['volume_percent']
    if current_volume <= 90:  # Evita definir o volume acima de 100
        sp.volume(current_volume + 10)
    else:
        sp.volume(100)

def diminuir_volume_spotify():
    current_volume = sp.current_playback()['device']['volume_percent']
    if current_volume >= 10:  # Evita definir o volume abaixo de 0
        sp.volume(current_volume - 10)
    else:
        sp.volume(0)
