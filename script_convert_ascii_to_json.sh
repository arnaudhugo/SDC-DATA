n=0
for file in `ls ./FICHIER/`; do
    var=$file".json"
    php convert_ascii_to_json.php /home/robinet/MSongsDB/PythonSrc/FICHIER/$file > ./FICHIERS_JSON/$var
    n=$((n+1))
    echo $n
done
