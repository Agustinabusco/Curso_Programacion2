import os
from moviepy import VideoFileClip, concatenate_videoclips

# Buscamos automáticamente cualquier archivo mp4 en la carpeta
archivos_mp4 = [f for f in os.listdir('.') if f.endswith('.mp4') and f != 'video_final_sin_audio.mp4']

if not archivos_mp4:
    print("Error: No encontré ningún video .mp4 en esta carpeta.")
else:
    nombre_entrada = archivos_mp4[0]
    nombre_salida = "video_final_sin_audio.mp4"
    print(f"Iniciando con el archivo: {nombre_entrada}")

    try:
        video = VideoFileClip(nombre_entrada)

        # Los pedazos que pediste
        clips = [
            video.subclipped(0, 48),           
            video.subclipped(82, 101),         
            video.subclipped(108, 135),        
            video.subclipped(159, 176),        
            video.subclipped(184)              
        ]

        video_final = concatenate_videoclips(clips)
        
        print("Procesando... esto puede llevar unos minutos.")
        video_final.write_videofile(nombre_salida, audio=False)
        
        print(f"¡Listo! Video creado: {nombre_salida}")
        video.close() # Cerramos para liberar el archivo

    except Exception as e:
        print(f"Error técnico: {e}")