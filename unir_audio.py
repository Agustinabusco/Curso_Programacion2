import os
from moviepy import VideoFileClip, AudioFileClip

# Nombres exactos de tus archivos actuales
nombre_video = "video_final_sin_audio.mp4"
nombre_audio = "ElevenLabs_2026-05-06T19_04_04_Brittney - Social Media Voice - Fun, Youthful & Informative_pvc_sp100_s50_sb75_se0_b_m2.mp3"

print("Iniciando proceso...")

try:
    # Cargamos archivos
    video = VideoFileClip(nombre_video)
    audio = AudioFileClip(nombre_audio)

    # Si el audio dura más que el video, lo recorta para que terminen juntos
    if audio.duration > video.duration:
        audio = audio.subclipped(0, video.duration)

    # Une el audio al video
    video_final = video.with_audio(audio)

    # Guarda el archivo nuevo
    nombre_salida = "tutorial_mermaid_final.mp4"
    video_final.write_videofile(nombre_salida, codec="libx264", audio_codec="aac")

    print(f"¡Terminado! Buscá el archivo: {nombre_salida}")

    video.close()
    audio.close()

except Exception as e:
    print(f"Error: {e}")