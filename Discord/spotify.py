import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials

# Suas credenciais do Spotify Developer
CLIENT_ID = os.getenv('CLIENT_ID_SPOTIFY')
CLIENT_SECRET = os.getenv('CLIENT_SECRET_SPOTIFY')

# Configurar a autenticação
auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

def get_musics(playlist_url):
    playlist_id = playlist_url.split("/")[-1].split("?")[0]

    # Buscar informações da playlist
    results = sp.playlist_items(playlist_id)

    # Extrair e imprimir os nomes das músicas
    music_list = []
    for item in results['items']:
        name_track = item['track']['name']
        first_artist_name = item['track']['artists'][0]['name']
        music_list.append(f"m!p {name_track} - {first_artist_name}")

    return music_list
