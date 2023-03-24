#! /bin/bash

sudo /usr/bin/python /home/balogh/Documents/light-control.py --on
/usr/bin/python /home/balogh/Documents/take-still.py
/usr/bin/python /home/balogh/Documents/get-conditions.py
sudo /usr/bin/python /home/balogh/Documents/light-control.py --off
