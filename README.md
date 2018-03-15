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

ENJOY !!
![alt tag](https://image.noelshack.com/fichiers/2018/11/4/1521133835-screen-shot-2018-03-15-at-18-09-45.png "Screen")

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

<pre>LOAD CSV WITH HEADERS FROM "file:/home/robinet/FATCSV.csv" AS row WITH row
MERGE (al:Album {album:row.album})
MERGE (a_id:Artist_id {artist_id:row.artist_id})
MERGE (a:Artist {artist:row.artist_name})
MERGE (d:Duration {duration:row.duration})
MERGE (t:Title {title:row.title})
MERGE (y:Year {year:row.year})

MERGE (a)<-[:PERFORMS]->(t)
MERGE (a_id)-[:ARTIST_ID]->(a)
MERGE (t)-[:RELEASE]->(y)
MERGE (al)-[:IN_ALBUM]->(t)
MERGE (a)-[:HAS_ALBUM]->(al)
MERGE (d)-[:DURATION]->(t)

FOREACH (TermName IN split(row.all_terms, ";") |
	MERGE (term:Term {Term:TermName})
	MERGE (t)-[:TERM]->(term))

FOREACH (ArtistsSimilar IN split(row.similar_artists, ";") |
	MERGE (a_id_similar:Artist_id_similar {Artist_id_similar:ArtistsSimilar})
	MERGE (a)-[:SIMILAR]->(a_id_similar))
RETURN count(*);</pre>
