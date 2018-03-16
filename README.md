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

<pre>WITH [ "ARV4KO21187FB38008", "ARWHM281187FB3D381", "ARJGOG11187B98D89F", "AR9ODB41187FB459B2", "ARXM6VQ1187FB5B1E0", "ARNWZ1N1187B9B71BA", "ARDWYZZ11F4C8413FA", "ARTP3H51187B98FB75", "ARWCDXN12454A4D1E8", "ARJ54S61187B9ACD39", "AR5PF241187B989C1D", "ARR7MLL1187B99B636", "ARLMHFV1187B9A3833", "ARPRERY1187B99E2DC", "AR34BCQ1187B9A68E4", "ARFWBUC11F4C8413DA", "ARPWGMN1187FB560E3", "ARVCIVW12454A4D1E7", "ARG89HY1187FB3CA15", "AR9IGU51187FB40D6B", "ARNNOYR11F4C845127", "ARZMFNT11F4C8413DD", "ARPR9W71187FB3723A", "AR5VBGP1187B98EB43", "ARFHDOI1187FB57230", "ARBSQPF11F4C8413E0", "AROYGID11F4C8413DB", "ARDXUGZ11F4C84452F", "ARMW4I01187B98AEF8", "AR7AYQG1187B994B3F", "ARHVZEM11F4C841FF9", "ARP9H0U1187FB3FEA7", "ARVSIGU11F4C8413E6", "AROWKNS1187FB59ED5", "ARUSTLW11F4C8413DE", "ARSKPDX11F4C83D2A9", "ARB4D891187B9954F7", "ARRIWD31187B9A9B4A", "ARNAAQH11F4C8413E1", "ARVRVYO11F4C8413DF", "ARNIZ5P1187B989AF5", "AR6YR7H1187FB40D23", "ARVAOCN12454A4CD5D", "ARQN3MO1187B98A811", "AR6M50Z1187B9A3503", "ARYEBOD11F4C83CD89", "ARQTORN11F50C4CED2", "ARUGOBE1269FCD74CE", "ARD3STO1187FB3E36A", "ARXU8YQ1187B999861", "AR0D3LM1187B9B9592", "ARCTCBU11F4C8413DC", "ARAVZPG1187B98F815", "AR79GH61187B993492", "ARBCGAP12086C13383", "ARLQK3P1187FB42113", "ARGNP1T1187FB5024D", "ARDIP5S1187FB57056", "ARWG53T1187FB44281", "ARV7RUN1187B9AF59C", "ARHAEF41187FB38ECB", "AR6UET41187B98C8BE", "ARYYFT91187FB50113", "ARD1KGL1187B98C838", "ARKBKTR1187FB39255", "ARRPOUR1187FB4D0BA", "AR6VXP71187FB5B898", "ARRWZGD11F50C4EDAE", "ARVCPYN11F4C83B19D", "AROKSCN1269FCD6CF1", "AR7YOK41187B9A3E0C", "ARSVLBA11F50C5126C", "ARGVYYD11C8A416342", "ARSK1IB1187B996850", "ARD39VZ1187B9B9A57", "ARIPNAN1187FB3E577", "ARK276D1187FB3D8FC", "AROWLBR11F4C84790E", "ARRX19M1187FB5756D", "ARLERFY11F50C4ABF2", "ARJ5PHW119B8668EB3", "ARQIMRI11F4C845124", "AR6S4EF1187B99A528", "ARYSPOI11F4C847915", "ARVFENS11F50C4ABE5", "ARTH9041187FB43E1F", "ARRZSQJ1269FB30A5F", "ARWFREB1187B98B09D", "ARZ3EIB1187B989D35", "ARNHXXE11F4C84129E", "ARACWVH1187FB55452", "AR3QS2R1187B9953C7", "ARTXGGI1187B9B3D58", "AR92C2I1187FB4161C", "ARNNCRQ11F50C4ABE7", "ARQPFMZ1187B9B1504", "ARPZEFW11F50C47E67", "ARSIEKZ122ECCBC0B1", "AR0WMTB1187B9A8E0F", "ARHRRWZ11F4C846224" ] AS Similar_Artists_List
UNWIND Similar_Artists_List AS Similar_Artist
WITH Similar_Artist
MATCH (n)
WHERE Similar_Artist = n.similar_a
RETURN Similar_Artist</pre>


ENJOY !!
![alt tag](https://i.imgur.com/eDyoxtj.jpg "Screen")
