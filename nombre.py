import os
import re

# Lista de patrones para detectar nombres de series, temporadas y episodios
patterns = [
    re.compile(r'Ver\s+(.+?)\s+(\d+)x(\d+)\s+online.*\.mp4$', re.IGNORECASE), 
    re.compile(r'^(.+?)\s*(\d+)x(\d+).*\.mp4$', re.IGNORECASE),
    re.compile(r'^([\w\.\s-]+?)\s*[\.\s]?(\d+)x(\d+)', re.IGNORECASE),
    re.compile(r'^([\w\.\s-]+?)\s*[\.\s]?(\d+)x(\d+)', re.IGNORECASE),
    re.compile(r'^(.+?)\.(\d+)x(\d+).*\.mp4$', re.IGNORECASE),
    re.compile(r'^(.+?)\s+(\d+)x(\d+).*$', re.IGNORECASE),
    re.compile(r'Ver (.*?) (\d+)x(\d+) online.*\.mp4$', re.IGNORECASE),
    re.compile(r'^([\w\.\s-]+?)\s*[\.\s]?(\d+)x(\d+)', re.IGNORECASE),
    re.compile(r'^(.+?)\.(\d+)x(\d+).*$', re.IGNORECASE),  
    re.compile(r'^(.+?)\.(\d+)x(\d+).*?(?:\.mkv)?\.mp4$', re.IGNORECASE),
    re.compile(r'^(.+?)\s*(\d+)x(\d+).*?at Streamtape\.com.*$', re.IGNORECASE),
    re.compile(r'^(.+?)\s*-\s*S(\d{2})E(\d{2}).*?(?:\.mkv)?(?:\.mp4)?(?:\s+at\s+Streamtape\.com)?$', re.IGNORECASE)

]

# Obtén la ruta del directorio donde está el script.
script_directory = os.path.dirname(os.path.abspath(__file__))

# Recorre todos los archivos en el directorio del script.
for filename in os.listdir(script_directory):
    if filename.lower().endswith('.mp4'):  # Filtra solo archivos .mp4
        for pattern in patterns:
            match = pattern.search(filename)
            if match:
                series_name = match.group(1).replace('.', ' ').strip()  # Reemplazar puntos por espacios
                season = match.group(2).zfill(2)  # Temporada con ceros a la izquierda
                episode = match.group(3).zfill(2)  # Episodio con ceros a la izquierda
                
                # Genera el nuevo nombre del archivo
                new_filename = f"{series_name} - S{season}E{episode}.mp4"
                
                # Obtén las rutas completas
                old_filepath = os.path.join(script_directory, filename)
                new_filepath = os.path.join(script_directory, new_filename)
                
                # Renombra el archivo
                os.rename(old_filepath, new_filepath)
                print(f'Renombrado: "{filename}" → "{new_filename}"')
                break  # Si encuentra un patrón válido, no revisa los demás