#!/usr/bin/env python 

#record the signal from the sensor

import time
import csv
from gpiozero import Button


sample_interval = 0.01  # seconds


def main():
    sensor = Button(23)  # pin 23 is a GPIO port

    start = time.time()

    fields = ['time', 'value']
    with open('trace1.csv', 'w', newline='') as tracefile:
        writer = csv.DictWriter(tracefile, fieldnames=fields)
        while True:
            now = time.time() - start
            if not sensor.is_pressed:
                p = 1.0
            else:
                p = 0.0
            writer.writerow({'time': now, 'value': p})

            time.sleep(sample_interval)

    return 0


if __name__ == "__main__":
    main()