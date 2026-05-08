from moviepy.editor import VideoFileClip, concatenate_videoclips

# 1. CAMBIÁ ESTO: Poné el nombre exacto de tu video (con el .mp4)
nombre_entrada = "video_informatica.mp4" 
nombre_salida = "video_editado_final.mp4"

print("Iniciando el proceso de edición...")

try:
    video = VideoFileClip(nombre_entrada)

    # 2. Definimos los segmentos que QUEREMOS conservar
    # Los cálculos de segundos ya están listos según lo que me pasaste
    clips = [
        video.subclip(0, 48),           # Inicio hasta 0:48
        video.subclip(82, 101),         # 1:22 hasta 1:41
        video.subclip(108, 135),        # 1:48 hasta 2:15
        video.subclip(159, 176),        # 2:39 hasta 2:56
        video.subclip(184)              # 3:04 hasta el final
    ]

    # 3. Unimos los fragmentos
    video_final = concatenate_videoclips(clips)
    
    # 4. Guardamos el resultado SIN audio
    print("Exportando video sin sonido... esto puede tardar un poquito.")
    video_final.write_videofile(nombre_salida, codec="libx264", audio=False)
    
    print(f"¡Listo! El video se guardó como: {nombre_salida}")

except Exception as e:
    print(f"Ocurrió un error: {e}")