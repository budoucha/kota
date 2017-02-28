while ! [ -e break ] ;do 
echo `date`: not yet.
python3 chkkota.py; 
done;

if [ -e ktkr ];then
echo `date`: ktkr!
python3 postMessage.py
fi

rm ktkr;
rm break;
rm ref_html
