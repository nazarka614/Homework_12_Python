from video_manager.media_player import Player
from video_manager.films_worker import Film
import os
import string

player_1 = Player("rickroll", "https://youtu.be/pqafKhbl1Rg?si=h7-REl3iYPCRtOnc", 777)
print(player_1.play("https://youtu.be/pqafKhbl1Rg?si=h7-REl3iYPCRtOnc"))
print(f"Video is playing: {player_1.playing}")
player_1.pause()
print(f"Video is playing: {player_1.playing}")

print(f"Current video quality: {player_1.quality}")
player_1.change_quality("4K")
print(f"Updated video quality: {player_1.quality}")

print(os.getcwd())
os.chdir("film_player")
print(os.getcwd())
os.mkdir("film_storage")
os.chdir("film_storage")
for letter in string.ascii_uppercase:
    os.mkdir(letter)

films = [
    Film("Inception", 2010),
    Film("The Shawshank Redemption", 1994),
    Film("The Dark Knight", 2008),
    Film("Pulp Fiction", 1994)
]

for i, film in enumerate(films, 1):
    print(f"Film {i} address: {film.get_film_address()}")
