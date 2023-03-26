#! /bin/bash

sudo /usr/bin/python /home/balogh/Documents/PHY-CAMERA2/light-control.py --on
/usr/bin/python /home/balogh/Documents/PHY-CAMERA2/take-still.py
/usr/bin/python /home/balogh/Documents/PHY-CAMERA2/get-conditions.py
sudo /usr/bin/python /home/balogh/Documents/PHY-CAMERA2/light-control.py --off
