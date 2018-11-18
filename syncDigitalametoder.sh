echo "Compiling site"

pelican content

echo "Rsyncing directory, please wait..."


rsync -vrP -e ssh output/ chrisk@genuskollen.se:/home/chrisk/digitalametoder.science/

echo "Then syncing the root folder and sub-directories"

rsync -vrP -e ssh . chrisk@genuskollen.se:/home/chrisk/digitalametoder.science/

echo "Done! Thank you...."
