
echo "Rsyncing directory, please wait..."

rsync -vrP -e ssh . chrisk@genuskollen.se:/home/chrisk/digitalametoder.science/


echo "Done! Thank you...."
