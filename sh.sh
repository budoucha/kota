while ! [ -e break ] ;do 
echo `date`: not yet.
python3 chkkota.py; 
sleep 300s; 
done;

if [ -e ktkr ];then
echo `date`: ktkr!
curl "https://slack.com/api/chat.postMessage?token=<TOKEN>&channel=<CHANNEL>&attachments=<MESSAGE>&pretty=1";
fi

rm ktkr;
rm break;
