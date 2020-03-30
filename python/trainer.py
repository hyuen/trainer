#!/usr/bin/env python 

import time
from gpiozero import Button


# set the circumference of the rolling part
circumference = 3.14 * 2.375  # inches
sample_interval = 0.01  # seconds
measure_threshold = 0.7


def main():
    sensor = Button(23)  # pin 23 is a GPIO port

    start = time.time()

    p = 0.0
    p_1 = 0.0
    alpha = 0.99   # coefficient of the low pass filter

    time_event_1 = 0
    time_event = 0

    while True:
        p_1 = p
        if not sensor.is_pressed:
            p = 1.0
        else:
            p = 0.0

        out = alpha * p_1 + (1 - alpha) * p

        # after the low pass filter, if the value is higher than the
        # threshold, consider a recording

        if out > measure_threshold:
            time_event_1 = time_event
            time_event = time.time() - start
            speed = circumference / (time_event - time_event_1)  # in / s
            speed = speed / 63360 * 3600
            print("Time [s]", time_event, "speed[mph]", speed)

        time.sleep(sample_interval)

    return 0


if __name__ == "__main__":
    main()
