from datetime import datetime
from notes.generator import get_random_instrument, get_random_notes
from audio.builder import build_audio

instrument = get_random_instrument()
notes = get_random_notes()

print("Instrumento:", instrument)
print("Notas:", notes)

# Generar timestamp para el nombre de archivo
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"output/sonido_{timestamp}.wav"

build_audio(instrument, notes, output_path=filename)