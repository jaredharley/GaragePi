# GaragePi
A Raspberry Pi living in my garage, doing garage things. Based off Drisocity's [Idiot's guide to a Raspberry Pi garage door opener][1].

## Part list
 - [Raspberry Pi B+](https://www.raspberrypi.org/products/model-b-plus/)
 - [Raspberry Pi camera module](https://www.raspberrypi.org/products/camera-module/)
 - [Magnetic switch](http://amzn.com/B0009SUF08) for detecting door position
 - [2 channel relay](http://amzn.com/B0057OC6D8) for triggering door open/close
 - [DHT11 temperature sensor](https://www.adafruit.com/products/386)

## Steps taken so far
 - Purchased supplies
 - Installed [WebIOPi 0.7.1][2]
 - WebIOPi installed [Weaved][3] (not sure if this will be needed or not)
 - [Disabled power management][4] on the wifi adapter
 - Connected sensors, relay, and LED lights on breadboard
 - Downloaded and installed [Adafruit_Python_DHT][6] to read the DHT11 sensor
 - Installed [WebPy][5] for the future web server.

## Disabling power management
 - Create a `8192cu.conf` file in `/etc/modprobe.d/`
 - Insert the following text:

```text
    # Disable power management
    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0 rtw_ips_mode=1
```

# Potential ideas
 - Add Raspi camera module
 - Add temperature sensor
 - Add logging capability (store ups/downs, possibly ip address of request?)
   - Include times when the garage is opened/closed, but the raspi isn't used
 - Push notifications
   - Door has been open more than x minutes
 

  [1]: http://www.driscocity.com/idiots-guide-to-a-raspberry-pi-garage-door-opener/
  [2]: http://webiopi.trouch.com/
  [3]: http://www.weaved.com/
  [4]: https://www.raspberrypi.org/forums/viewtopic.php?t=61665
  [5]: http://webpy.org
  [6]: https://github.com/adafruit/Adafruit_Python_DHT
