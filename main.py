from notes.generator import get_random_instrument, get_random_notes
from audio.builder import build_audio

instrument = get_random_instrument()
notes = get_random_notes()

print("Instrumento:", instrument)
print("Notas:", notes)

build_audio(instrument, notes, output_path="output/sonido.wav")