import os
import re

# Define un patrón de expresión regular para detectar los archivos que coincidan con el formato deseado.
pattern = re.compile(r'Ver (.*?) (\d+)x(\d+) online.*\.mp4$', re.IGNORECASE)

# Obtén la ruta del directorio donde está el script.
script_directory = os.path.dirname(os.path.abspath(__file__))

# Recorre todos los archivos en el directorio del script.
for filename in os.listdir(script_directory):
    if filename.endswith('.mp4'):  # Filtra solo archivos .mp4
        match = pattern.search(filename)
        if match:
            series_name = match.group(1).strip()  # Nombre de la serie
            season = match.group(2).zfill(2)       # Temporada (con ceros a la izquierda si es necesario)
            episode = match.group(3).zfill(2)      # Episodio (con ceros a la izquierda si es necesario)
            
            # Genera el nuevo nombre del archivo en el formato deseado.
            new_filename = f"{series_name} - S{season}E{episode}.mp4"
            
            # Obtén la ruta completa de los archivos originales y los renombrados.
            old_filepath = os.path.join(script_directory, filename)
            new_filepath = os.path.join(script_directory, new_filename)
            
            # Renombra el archivo.
            os.rename(old_filepath, new_filepath)
            print(f'Renombrado: "{filename}" a "{new_filename}"')
