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
<pre>$> find -name "*.h5" -exec cp {} ./ALL_FILES/FICHIERS_H5/ \;</pre>
Pour être sur d'avoir le bon nombre utilisez :
<pre>$> ls ./DOSSIER | wc -l</pre>

# Etape 2
Utilisez 'script_python_h5_to_ascii.sh' pour lancer le script pyhon 'display_song.py' :
<pre>$> sh script_python_h5_to_ascii.sh</pre>
Exemple de fichier générer dans le dossier /ALL_FILES/FICHIERS_ASCII/.

# Etape 3
Utilisez 'script_convert_ascii_to_json.sh' pour lancer le script php 'convert_ascii_to_json.php' :
<pre>$> sh script_convert_ascii_to_json.sh</pre>
Exemple de fichier générer dans le dossier /ALL_FILES/FICHIERS_JSON/.

Uptade : Le script 'script_convert_ascii_to_json.sh' créer un seul fichier contenant toutes les data 'ALL_DATA_JSON.json'

# Etape 4

On utilise le site :
<pre>https://codebeautify.org/json-to-csv</pre>
Exemple de fichier générer dans le dossier ALL_DATA_CSV.csv.

# Neo4J
# Etape 1

Pour installer 'openjdk-8-jre-headless' :
<pre># En Root :
$> echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

$> sudo apt-get update
$> sudo apt-get install -t jessie-backports openjdk-8-jre-headless</pre>

Installation :
<pre>$> wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key add -
$> echo 'deb http://debian.neo4j.org/repo stable/' > /tmp/neo4j.list
$> mv /tmp/neo4j.list /etc/apt/sources.list.d

$> apt-get update
$> apt-get install neo4j=3.1.4

$> service neo4j status</pre>

Configuration :
<pre>$> nano /etc/neo4j/neo4j.conf 

# Décommentez :
dbms.security.auth_enabled=false
dbms.security.allow_csv_import_from_file_urls=true

# Décommentez et modifiez :
dbms.connector.bolt.listen_address=0.0.0.0:7687
dbms.connector.http.listen_address=YOUR_IP:7474

# Commentez :
#dbms.directories.import=/var/lib/neo4j/import</pre>

<pre>$> service neo4j restart</pre>

Allez sur : http://YOUR_IP:7474/browser/

# Etape 2

<pre>LOAD CSV WITH HEADERS FROM "file:/ALL_FILES/CSV/artists_id.csv" AS row
CREATE (a:Artist {artist_id:row.artist_id})</pre>

<pre>LOAD CSV WITH HEADERS FROM "file:/ALL_FILES/CSV/genres.csv" AS row
CREATE (g:Genre {name:row.mbtag})</pre>

<pre>LOAD CSV WITH HEADERS FROM "file:/ALL_FILES/CSV/artist_genre.csv" AS row
MATCH (a:Artist {artist_id:row.artist_id}), (g:Genre {name:row.mbtag})
MERGE (a)-[:HAS_GENRE]->(g)</pre>

<pre>USING PERIODIC COMMIT 50
LOAD CSV WITH HEADERS FROM "file:/ALL_FILES/CSV/ALL_DATA_CSV.csv" AS row

MERGE (m:Music {title: row.title, duration: row.duration})
WITH m, row
MATCH (a:Artist {artist_id:row.artist_id})
MERGE (a)-[:OWNS]->(m)
SET a.name = row.artist_name

MERGE (y:Year {year: row.year})
MERGE (m)-[:RELEASED_IN]->(y)

MERGE (al:Album {name:row.album})
MERGE (m)-[:IN]->(al)
MERGE (a)-[:CREATED]->(al)

WITH a, m, row

UNWIND split(row.all_terms, ';') as genre_instance
MATCH (g:Genre {name:genre_instance})
MERGE (m)-[:HAS_GENRE]->(g)

WITH a, m, row

UNWIND split(row.similar_artists, ';') as asi
MATCH (as:Artist {artist_id:asi})
MERGE (a)-[:SIMILAR_TO]->(as)

RETURN count(*);</pre>

Schéma des liaisons :
![alt tag](https://image.noelshack.com/fichiers/2018/12/2/1521576874-schema.jpg "Screen")

Augmenter le nombres de nodes affichable dans Neo4j :
<pre>:config initialNodeDisplay: 10000</pre>

ENJOY !!
![alt tag](https://i.imgur.com/eDyoxtj.jpg "Screen")

# API 

# Etape 1

Installation :

<pre>$> apt-get install python-pip</pre>
<pre>$> pip install bottle</pre>
<pre>$> pip install neo4jrestclient</pre>

# Etape 2 - ROUTES

Récupérer tout les genres :
<pre>http://YOUR_IP:5000/api/all/genre/'YOUR_API_KEY'</pre>

Récupérer 'nombre' musiques random :
<pre>http://YOUR_IP:5000/api/random/'nombre'/'YOUR_API_KEY'</pre>

Récupérer l'artiste et le titre des musiques en fonction du 'genre' et du 'nombre' de musique voulu :
<pre>http://YOUR_IP:5000/api/genre/'genre'/'number'/'YOUR_API_KEY'</pre>

Récupérer le 'nombre' voulu de titre d'un artiste (s'il y en à plusieurs) :
<pre>http://YOUR_IP:5000/api/artist/'artist_name'/'number'/'YOUR_API_KEY'</pre>
