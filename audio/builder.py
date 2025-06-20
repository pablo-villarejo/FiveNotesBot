# audio/builder.py

from pydub import AudioSegment
import os

SAMPLES_DIR = "samples"  # raíz donde tienes las carpetas de instrumentos

def build_audio(instrument: str, notes: list[str], output_path="output/sonido.wav"):
    audio = AudioSegment.silent(duration=0)

    for note in notes:
        path = os.path.join(SAMPLES_DIR, instrument, f"{note}.wav")
        if not os.path.isfile(path):
            print(f"[!] Archivo no encontrado: {path}")
            continue

        sample = AudioSegment.from_wav(path)
        audio += sample

    # Agregar 1s de silencio al inicio y al final
    silence = AudioSegment.silent(duration=1000)  # 1s
    final_audio = silence + audio + silence

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_audio.export(output_path, format="wav")
    print(f"[✔] Audio generado: {output_path}")
