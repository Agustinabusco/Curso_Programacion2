import os
from moviepy import VideoFileClip, AudioFileClip

# Buscamos el video y el audio automáticamente en la carpeta
archivos_mp4 = [f for f in os.listdir('.') if f.endswith('.mp4') and 'final' not in f]
archivos_audio = [f for f in os.listdir('.') if f.endswith(('.mp3', '.wav', '.m4a'))]

if not archivos_mp4 or not archivos_audio:
    print("Error: Asegurate de tener un archivo .mp4 y uno de audio (.mp3, .wav) en la carpeta.")
else:
    video_nom = archivos_mp4[0]
    audio_nom = archivos_audio[0]
    
    print(f"Uniendo {video_nom} con el audio {audio_nom}...")

    try:
        # Cargamos el video y el audio
        video_clip = VideoFileClip(video_nom)
        audio_clip = AudioFileClip(audio_nom)

        # Si el audio es más largo que el video, lo cortamos para que coincidan
        if audio_clip.duration > video_clip.duration:
            audio_clip = audio_clip.subclipped(0, video_clip.duration)

        # Le ponemos el audio al video
        video_con_audio = video_clip.with_audio(audio_clip)

        # Guardamos el resultado
        nombre_resultado = "video_con_voz_final.mp4"
        video_con_audio.write_videofile(nombre_resultado, codec="libx264", audio_codec="aac")

        print(f"¡Listo! El video final es: {nombre_resultado}")
        
        # Cerramos los archivos
        video_clip.close()
        audio_clip.close()

    except Exception as e:
        print(f"Hubo un error: {e}")