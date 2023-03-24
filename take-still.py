from picamera2 import Picamera2, Preview, Metadata
from libcamera import controls
import time, datetime

still_save_path="/media/balogh/SAMSUNG_T5/stills-001/"
web_save_path="/var/www/physarum.net/public_html/"
picam2 = Picamera2()
still_config = picam2.create_still_configuration()
web_config = picam2.create_still_configuration(main={"size":(800,600)})
picam2.start(show_preview=True)
picam2.autofocus_cycle()
time.sleep(1)
dt = datetime.datetime.now()
datestring = dt.strftime("%Y%m%dT%H%M")
picam2.switch_mode_and_capture_file(still_config,still_save_path+"still-"+datestring+".png")
picam2.switch_mode_and_capture_file(web_config,web_save_path+"still.png")
