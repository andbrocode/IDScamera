#!/bin/python3
#
# this script takes images of the IDS camera
# connected via USB and stores them in a local
# directory
#
#
# adopted by Andreas Brotzer (2024)
#
# ----------------------------------------------

import os
from pyueye import ueye
from datetime import datetime
from time import sleep

# configurations
path_to_images = "/home/pi/IDS/images/"

exposure = 200 # milli seconds

gain = 0 # percent

# initialize ids camera
hcam = ueye.HIDS(0)
pccmem = ueye.c_mem_p()
memID = ueye.int()

ueye.is_InitCamera(hcam, None)
nret = ueye.is_ResetToDefault(hcam)

if nret == ueye.IS_SUCCESS:
	print("-> ResetToDefault: Done")
else:
	print("-> ResetToDefault: FAILED")

# initialize sensor info object
sensorinfo = ueye.SENSORINFO()
# get sensor information
ueye.is_GetSensorInfo(hcam, sensorinfo)

# print("-> Sensor Info: \n", sensorinfo)
print(f"-> Camera Name: {sensorinfo.strSensorName.decode('utf-8')}")

# set exposure
nret = ueye.is_Exposure(hcam, ueye.IS_EXPOSURE_CMD_SET_EXPOSURE, ueye.double(exposure), ueye.sizeof(ueye.double(exposure)))
if nret == ueye.IS_SUCCESS:
        print(f"-> SetExposure={exposure}: Done")
else:
        print(f"-> SetExposure={exposure}: FAILED")

# set master gain
nret = ueye.is_SetHardwareGain(hcam, gain, ueye.IS_IGNORE_PARAMETER, ueye.IS_IGNORE_PARAMETER, ueye.IS_IGNORE_PARAMETER)
if nret == ueye.IS_SUCCESS:
        print(f"-> SetHardwareGain={gain}: Done")
else:
        print(f"-> SetHardwareGain={gain}: FAILED")


# ACHTUNG COLORMODE beachten 8 / 24 / 32
# UI-3360CP-M --> 8Bit
# UI_3250CP-C --> 32Bit  24 funktioniert nicht auf Anhieb
nret = ueye.is_AllocImageMem(hcam, sensorinfo.nMaxWidth, sensorinfo.nMaxHeight, 8, pccmem, memID)
if nret == ueye.IS_SUCCESS:
	print("-> AllocImageMemory: Done")
else:
	print("-> AllocImageMemory: FAILED")

# set image memory
nret = ueye.is_SetImageMem(hcam, pccmem, memID)
if nret == ueye.IS_SUCCESS:
        print("-> SetImageMemory: Done")
else:
        print("-> SetImageMemory: FAILED")
#print(nret, pccmem, memID)

# stop video stream
nret = ueye.is_FreezeVideo(hcam, ueye.IS_DONT_WAIT)
if nret == ueye.IS_SUCCESS:
        print("-> FreezeVideo: Done")
else:
        print("-> FreezeVideo: FAILED")

# specify filename
dt_utc = datetime.utcnow()
date0 = dt_utc.date().isoformat().replace("-","")
time0 = dt_utc.time().isoformat().replace(":","").split(".")[0]
filename = f"{date0}_{time0}.png"

if not os.path.isdir(path_to_images+date0):
	os.mkdir(path_to_images+date0+"/")

# pause
sleep(1)

# create image file parameter object
FileParams = ueye.IMAGE_FILE_PARAMS()
# set filename
FileParams.pwchFileName = path_to_images+date0+"/"+filename
# set file type
FileParams.nFileType = ueye.IS_IMG_PNG
# set image memory
FileParams.ppcImageMem = None
# set image ID
FileParams.pnImageID = None

# create screenshot image
nret = ueye.is_ImageFile(hcam, ueye.IS_IMAGE_FILE_CMD_SAVE, FileParams, ueye.sizeof(FileParams))
if nret == ueye.IS_SUCCESS:
	print(f"-> ImageFile: {filename}")
else:
	print("-> ImageFile: FAILED")

# free image memorey
ueye.is_FreeImageMem(hcam, pccmem, memID)

# exit the camera
ueye.is_ExitCamera(hcam)

print("\nDONE\n")

# End of File
