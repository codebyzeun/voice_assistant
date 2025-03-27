import os
import random


def play_music():
    music_folder = "audio/"
    music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

    if music_files:
        song = random.choice(music_files)
        os.system(f"start {os.path.join(music_folder, song)}")
        return f"Playing your favorite music: {song}"
    else:
        return "No music files found in the audio directory."
