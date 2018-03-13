#python ./display_song.py /home/robinet/Million-Song-Dataset-HDF5-to-CSV/LES_FICHIER_DE_FDP/TRAAAAW128F429D538.h5

n=0
for file in `ls /home/robinet/MSongsDB/PythonSrc/FICHIER/`; do
    var=$file".json"
    php convert_ascii_to_json.php /home/robinet/MSongsDB/PythonSrc/FICHIER/$file > ./FICHIERS_JSON/$var
    n=$((n+1))
    echo $n
done
