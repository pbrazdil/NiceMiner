from py3nvml.py3nvml import *

def numberOfGPUs():
    nvmlInit()
    return nvmlDeviceGetCount()