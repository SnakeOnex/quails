import serial
import time
import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)  # Adjust the device name and baud rate
last_log_time = time.time()

def log_temperature(temp):
    with open('temperature.csv', 'a') as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp},{temp}\n')

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        temp = float(line)
        print(temp)

        if time.time() - last_log_time > 60 * 10:
            log_temperature(temp)

        time.sleep(1)
