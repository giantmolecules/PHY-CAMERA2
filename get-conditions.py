import smbus2
import bme280
import time
import datetime
import csv

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

log_path="/media/balogh/SAMSUNG_T5/conditions/"
web_path="/var/www/physarum.net/public_html/"

# the sample method will take a single reading and return a
# compensated_reading object
data = bme280.sample(bus, address, calibration_params)

# the compensated_reading class has the following attributes
# print(data.id)
# print(data.timestamp)
# print(data.temperature)
# print(data.pressure)
# print(data.humidity)

# there is a handy string representation too
# print(data)

temp = round(data.temperature,2)
humid = round(data.humidity,2)
press = round(data.pressure,2)

with open('/media/balogh/SAMSUNG_T5/conditions/conditions.csv', 'a') as csvfile:
    x = datetime.datetime.now()
    xf = x.strftime("%Y%m%dT%H%M")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow([xf,temp, humid, press])
    csvfile.close()

with open('/var/www/physarum.net/public_html/current-conditions.html', 'w') as myfile:
    myfile.write("<html><div class=conditions>Time: "+xf+" Temp: "+str(temp)+" C Humidity: "+str(humid)+" % Pressure: "+str(press)+" hPa</div>")
    myfile.close()

