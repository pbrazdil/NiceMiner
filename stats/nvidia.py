from py3nvml.py3nvml import *
import py3nvml.nvidia_smi as smi

def printGPUs():
    nvmlInit()
    print("Driver Version: {}".format(nvmlSystemGetDriverVersion()))

    deviceCount = nvmlDeviceGetCount()
    for i in range(deviceCount):
        handle = nvmlDeviceGetHandleByIndex(i)
        powDraw = (nvmlDeviceGetPowerUsage(handle) / 1000.0)
        print("Device {}: {}".format(i, nvmlDeviceGetName(handle)), '%.2f W' % powDraw)