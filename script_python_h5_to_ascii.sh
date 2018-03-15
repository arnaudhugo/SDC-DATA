n=0
for file in `ls /ALL_FILES/FICHIERS_H5/`; do
    var=$file".txt"
    python ./display_song.py /ALL_FILES/FICHIERS_H5/$file > /ALL_FILES/FICHIERS_ASCII/$file.txt
    n=$((n+1))
    echo $n
done
