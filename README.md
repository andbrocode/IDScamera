# IDS Camera

Run IDS camera with RaspberryPi4 (image with Debian Bookworm 32bit)



Information by IDS is provided here: https://en.ids-imaging.com/files/downloads/ids-software-suite/readme/ueye-linux-embedded-readme-49200_EN.html#system-requirements

1) Download SDK package from IDS ( https://en.ids-imaging.com/download-details/AB00514.html ): <br>
   ids-software-suite-linux-armhf-4.96.1-archive.tgz <br>
   (you will need to create an account at IDS for this)

3) Unpack the archive:  <code> tar -xvf ids-software-suite-linux-armhf-4.96.1-archive.tgz  </code>

4) Install packages: <br>
    <code> sudo apt install libgomp1 udev libpng-dev libjpeg-dev libopenblas0 libomp5  </code> <br>
    <code> sudo apt install libc6 libstdc++6 libqt5widgets5 libqt5gui5 libqt5opengl5 libqt5concurrent5 build-essential libcap2 libusb-1.0-0 libqt5xml5 libqt5network5  </code>
   
6) Install pip3 for python3: <code>  sudo apt install python3-pip </code> 

7) Move the unrequired file:  <code> sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED </code>

8) Install python packages:  <code> pip3 install pyueye numpy  </code>

9) Go to the directory of the unpacked archive of 3) and run:   <code> sudo ./ueye_4.96.1.2054_armhf.run  </code>

This should have ideally installed the drivers of the IDS suite. The daemons should run as active: <br>
USB: <code> sudo systemctl status ueyeusbdrc </code> (for camera via USB) <br>
ETH: <code> sudo systemctl status ueyeethdrc </code> (for camera via ETH)

To test it, one can run:  <code> ueyedemo  </code> or  <code> ueyesetid  </code>

To uninstall run:   <code> sudo ueyesetup -u all  </code>
    

The ids camera should now be reckognized and operational. With a screen one can use <code> ueyedemo </code> to see a live stream of the camera with a GUI.

To take a snapshot with python with use the script: <code> ueye_screenshot.py </code>
This script takes a snapshot of the camera stream and stores it as a .png image file at:  ** ./images/<date>/<date>_<time>.png **
Using a simple cronjob turns this into a automatic snapshot routine.
