# Monitor cadence on a stationary bicycle trainer

This project uses a Raspberry Pi Zero and an Infrared Sensing Module to make a smart Trainer



## Materials
 * Bicycle trainer. [For example](https://www.amazon.com/gp/product/B076LZG1KZ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
 * Raspberry Pi Zero
 * IR Sensor
 * Electric tape
 * Debouncer circuit: 2 5k Ohm resistors, 0.01 uF Capacitor
 * LEDs for debugging: LED + 330 Ohm resistors

## Instructions
 * Place the IR sensor in a position like ![diag1](https://github.com/hyuen/trainer/blob/master/pictures/IMG_9845.jpeg) 
 * Connect the output of the sensor to a GPIO pin of the PiZero. You will need to add a debouncer circuit to avoid spurious measurements.
 * Run trainer.py

## Electric diagram

TODO

 * Sample picture of the circuit: ![diag2](https://github.com/hyuen/trainer/blob/master/pictures/IMG_9846.jpeg)
 
## Sample output

After getting the output, it can be plotted as this

![](https://github.com/hyuen/trainer/blob/master/python/tracker.png)

## Final setting

![](https://github.com/hyuen/trainer/blob/master/pictures/IMG_9848.jpeg)

## Issues
 * Fix the settings on the debouncer circuit
 * Fix the settings of the Low Pass filter in trainer.py
 * Generate plots automatically
 * Plug to Strava
