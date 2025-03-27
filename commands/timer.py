import time

def set_timer(duration_in_seconds):
    tts.speak(f"Timer set for {duration_in_seconds} seconds.")
    time.sleep(duration_in_seconds)
    tts.speak(f"Time's up! {duration_in_seconds} seconds have passed.")
