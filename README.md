# IDScamera
Run IDS camera with RaspberryPi4



Information by IDS is provided here: https://en.ids-imaging.com/files/downloads/ids-software-suite/readme/ueye-linux-embedded-readme-49200_EN.html#system-requirements

1) Download SDK package from IDS ( https://en.ids-imaging.com/download-details/AB00514.html ):  ids-software-suite-linux-arm64-4.96.1-archive.tgz
   (you will need to create an account at IDS for this)

3) Unpack the archive:  tar -xvf ids-software-suite-linux-armhf-4.96.1-archive.tgz

4) Install packages:
   sudo apt install libgomp1 udev libpng-dev libjpeg-dev libopenblas0 libomp5
   sudo apt install libc6 libstdc++6 libqt5widgets5 libqt5gui5 libqt5opengl5 libqt5concurrent5 build-essential libcap2 libusb-1.0-0 libqt5xml5 libqt5network5
   
6) Install pip3 for python3:  sudo apt install python3-pip

7) Move the unrequired file:  sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED ~/Downloads/

8) Install python packages:  pip3 install pyueye numpy

9) Go to the directory of the unpacked archive of 3) and run:  sudo ./ueye_4.96.1.2054_arm64.run

10) 
    
