echo "Compiling site"

pelican content


echo "Rsyncing directory, please wait..."

rsync -vrP -e ssh output/ chrisk@genuskollen.se:/home/chrisk/digitalametoder.science/

echo "Done! Thank you...."

