#python ./display_song.py /home/robinet/Million-Song-Dataset-HDF5-to-CSV/LES_FICHIER_DE_FDP/TRAAAAW128F429D538.h5

for file in `ls /home/robinet/Million-Song-Dataset-HDF5-to-CSV/LES_FICHIER_DE_FDP/`; do
    var=$file".txt"
    python ./display_song.py /home/robinet/Million-Song-Dataset-HDF5-to-CSV/LES_FICHIER_DE_FDP/$file > ./FICHIER/$file.txt
done
