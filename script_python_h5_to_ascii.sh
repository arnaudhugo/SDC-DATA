for file in `ls ./FOLDER_WITH_ALL_H5_FILE/`; do
    var=$file".txt"
    python ./display_song.py ./FOLDER_WITH_ALL_H5_FILE/$file > ./FICHIER/$file.txt
done
