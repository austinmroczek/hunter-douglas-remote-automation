# hunter-douglas-remote-automation
Automate a Hunter Douglas Platinum remote for home automation purposes.

### Basic Steps ###
* Modify remote electronics for computer based control (requires soldering)
* Control remote locally with Raspberry Pi
* Control remote via LAN with Raspberry Pi

### Credits ###

* Electrical mods to the remote based on efforts of Ryan Wright at http://www.ryanwright.com/ht/powerrise/
* Remote user guide at https://cdn2.hunterdouglas.com/static/documents/remote-control-guide.pdf

### Hardware Requirements ###
* Hunter Douglas Platinum remote
* Raspberry Pi
* Wire and soldering equipment

### Software Requirements ###
* Python 3.5
* gpiozero [https://gpiozero.readthedocs.io/en/stable/index.html]

## Modify Remote Electronics ##

Generally follow directions from Ryan Wright at http://www.ryanwright.com/ht/powerrise/

Instead of creating a new remote box with new buttons, wire to a set of relays that can be controlled by a computer.

## Control Remote Locally ##

First step in making sure everything works is to operate the blinds from the local machine.  I used a Raspberry Pi and it's GPIO pins.

## Control Remote via LAN ##

Add a simple HTTP server so you can control your remote from your Local Area Network.  I suppose you could make this accessible outside the LAN if you want.

The current program includes this capability.

## Run at system startup ##
Run the systemd-setup.sh script to enable the program to run automatically at system startup.  It assumes user is "pi" and runs with the permissions of that user.

## Future / To-do ##
* Increase security
* Better tie to Home Assistant or other home automation capabilities
 