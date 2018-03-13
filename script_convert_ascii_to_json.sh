n=0
for file in `ls ./FICHIER/`; do
    var=$file".json"
    php convert_ascii_to_json.php ./FICHIER/$file > ./FICHIERS_JSON/$var
    n=$((n+1))
    echo $n
done
