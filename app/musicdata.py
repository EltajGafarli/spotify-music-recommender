import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from random import randint

client_id = 'ea070e2abec3424d907edff3255acec7'

client_secret = '1d9aa5a40292427c8fc4cd1def948e14'


def getMusics():
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret))
    genres = spotify.recommendation_genre_seeds()
    seed_genres = genres["genres"][randint(0,len(genres["genres"]))-1]
    results = spotify.recommendations(seed_genres=[seed_genres],limit=27)

    return results,seed_genres