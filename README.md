# SDC-DATA

Pour récupérer les fichier 'display_song.py' et 'hdf5_getters.py' :
<pre>https://github.com/tbertinmahieux/MSongsDB</pre>
Merci à lui.

Pour télécharger les Datasets (MillionSongSubset 10 000 songs) :
<pre># Direct download :
http://static.echonest.com/millionsongsubset_full.tar.gz

# Depuis le site :
https://labrosa.ee.columbia.edu/millionsong/pages/getting-dataset#subset</pre>

# Extraction des données depuis les Datasets
# Etape 1
Pour copier tout les fichier .h5 dans le même dossier :
<pre>$> find -name "*.h5" -exec cp {} ./DESTINATION \;</pre>
Pour être sur d'avoir le bon nombre utilisez :
<pre>$> ls ./DOSSIER | wc -l</pre>

# Etape 2
Utilisez 'script_python_h5_to_ascii.sh' pour lancer le script pyhon 'display_song.py' :
<pre>$> sh script_python_h5_to_ascii.sh</pre>
Exemple de fichier générer dans le dossier FICHIER.

# Etape 3
Utilisez 'script_convert_ascii_to_json.sh' pour lancer le script php 'convert_ascii_to_json.php' :
<pre>$> sh script_convert_ascii_to_json.sh</pre>
Exemple de fichier générer dans le dossier FICHIERS_JSON.

# Etape 4
Convert JSON to CSV.
Script soon.

# Neo4J
# Etape 1

Pour installer 'openjdk-8-jre-headless' :
<pre># En Root :
$> echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

$> sudo apt-get update
$> sudo apt-get install -t jessie-backports openjdk-8-jre-headless</pre>

Installation :
<pre>$> wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
$> echo 'deb http://debian.neo4j.org/repo stable/' >/tmp/neo4j.list
$> mv /tmp/neo4j.list /etc/apt/sources.list.d

$> apt-get update
$> apt-get install neo4j=3.1.4

$> service neo4j status</pre>

Configuration :
<pre>$> nano /etc/neo4j/neo4j.conf 

# Décommentez :
dbms.security.auth_enabled=false

# Décommentez et modifiez :
dbms.connector.bolt.listen_address=0.0.0.0:7687
dbms.connector.http.listen_address=YOUR_IP:7474</pre>

Allez sur : http://YOUR_IP:7474/browser/
