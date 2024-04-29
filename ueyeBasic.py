from pyueye import ueye
import time

# declaration of some used variables
hcam = ueye.HIDS(0)
pccmem = ueye.c_mem_p()
memID = ueye.int()


ueye.is_InitCamera(hcam, None)
nret = ueye.is_ResetToDefault(hcam)
print(nret)

sensorinfo = ueye.SENSORINFO()
ueye.is_GetSensorInfo(hcam, sensorinfo)

# ACHTUNG COLORMODE beachten 8 / 24 / 32
# UI-3360CP-M --> 8Bit
# UI_3250CP-C --> 32Bit  24 funktioniert nicht auf Anhieb
nret = ueye.is_AllocImageMem(hcam, sensorinfo.nMaxWidth, sensorinfo.nMaxHeight, 8, pccmem, memID)
print(nret)
nret = ueye.is_SetImageMem(hcam, pccmem, memID)
#print(nret, pccmem, memID)
nret = ueye.is_FreezeVideo(hcam, ueye.IS_DONT_WAIT)
print(nret)
time.sleep(1)
FileParams = ueye.IMAGE_FILE_PARAMS()
FileParams.pwchFileName = "pythontestimage.png"
FileParams.nFileType = ueye.IS_IMG_PNG
FileParams.ppcImageMem = None
FileParams.pnImageID = None

nret = ueye.is_ImageFile(hcam, ueye.IS_IMAGE_FILE_CMD_SAVE, FileParams, ueye.sizeof(FileParams))
print(nret)
ueye.is_FreeImageMem(hcam, pccmem, memID)
ueye.is_ExitCamera(hcam)
