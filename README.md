# Monitor cadence on a stationary bicycle trainer

This project uses a Raspberry Pi Zero and an Infrared Sensing Module

## Materials
 * Bicycle trainer. [For example](https://www.amazon.com/gp/product/B076LZG1KZ/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1)
 * Raspberry Pi Zero
 * IR Sensor
 * Electric tape

## Instructions
 * Place the IR sensor in a position like ![diag1](https://github.com/hyuen/trainer/blob/master/pictures/IMG_9845.jpeg) 
 * Connect the output of the sensor to a GPIO pin of the PiZero. You will need to add a debouncer circuit to avoid spurious measurements.
 * Run trainer.py

## Sample output

After getting the output, it can be plotted as this

![](https://github.com/hyuen/trainer/blob/master/python/tracker.png)


