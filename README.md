# GaragePi
A Raspberry Pi living in my garage, doing garage things. Based off Drisocity's [Idiot's guide to a Raspberry Pi garage door opener][1].

# Steps taken
 - Purchased supplies
 - Installed [WebIOPi 0.7.1][2]
 - WebIOPi installed [Weaved][3] (not sure if this will be needed or not)
 - [Disabled power management][4] on the wifi adapter

## Disabling power management
 - Create a `8192cu.conf` file in `/etc/modprobe.d/`
 - Insert the following text:

```text
    # Disable power management
    options 8192cu rtw_power_mgnt=0 rtw_enusbss=0 rtw_ips_mode=1
```

  [1]: http://www.driscocity.com/idiots-guide-to-a-raspberry-pi-garage-door-opener/
  [2]: http://webiopi.trouch.com/
  [3]: http://www.weaved.com/
  [4]: https://www.raspberrypi.org/forums/viewtopic.php?t=61665
