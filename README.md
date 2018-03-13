# SDC-DATA

Pour récupérer les fichier 'display_song.py' et 'hdf5_getters.py' :
<pre>https://github.com/tbertinmahieux/MSongsDB</pre>
Merci à lui.

# Etape 1
Pour copier tout les fichier .h5 dans le même dossier :
<pre>$> find -name "*.h5" -exec cp {} ./DESTINATION \;</pre>

# Etape 2
Utilisez 'script_python_h5_to_ascii.sh' pour lancer le script pyhon 'display_song.py' :
<pre>$> sh script_python_h5_to_ascii.sh</pre>
Exemple de fichier générer dans le dossier FICHIER.

# Etape 3
Utilisez 'script_convert_ascii_to_json.sh' pour lancer le script php 'convert_ascii_to_json.php' :
<pre>$> sh script_convert_ascii_to_json.sh</pre>
Exemple de fichier générer dans le dossier FICHIERS_JSON.
