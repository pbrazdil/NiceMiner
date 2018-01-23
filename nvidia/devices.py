from py3nvml.py3nvml import *

def count():
    nvmlInit()
    return nvmlDeviceGetCount()

def get_driver_version():
    nvmlInit()
    return nvmlSystemGetDriverVersion()

def get():
    nvmlInit()
    deviceCount = nvmlDeviceGetCount()

    res = []
    for i in range(deviceCount):
        handle = nvmlDeviceGetHandleByIndex(i)
        res.append([handle, nvmlDeviceGetName(handle), nvmlDeviceGetPowerUsage(handle) / 1000.0])

    return res

def reset():
    # sudo nvidia-smi --gpu-reset -i 0
    pass
    