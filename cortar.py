from moviepy import VideoFileClip, concatenate_videoclips

# Poné el nombre exacto de tu video
nombre_entrada = "tu_video.mp4" 
nombre_salida = "video_final_sin_audio.mp4"

print("Iniciando...")

try:
    video = VideoFileClip(nombre_entrada)

    # Segmentos que queremos mantener
    clips = [
        video.subclipped(0, 48),           
        video.subclipped(82, 101),         
        video.subclipped(108, 135),        
        video.subclipped(159, 176),        
        video.subclipped(184)              
    ]

    video_final = concatenate_videoclips(clips)
    
    print("Procesando el video final...")
    video_final.write_videofile(nombre_salida, audio=False)
    
    print(f"¡Éxito! Archivo creado: {nombre_salida}")

except Exception as e:
    print(f"Error: {e}")