clear
echo "kota: Kota observes then alerts."
python3 init.py
nohup sh sh.sh > out.log  2> err.log &
