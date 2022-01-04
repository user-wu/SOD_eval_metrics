# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

_RGB_SOD_ROOT = "D:\Projects\PySODMetrics\data\data_label"

ECSSD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "ECSSD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "mask"), suffix=".png"),
)
DUTOMRON = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "mask"), suffix=".png"),
)
HKUIS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "HKU-IS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "image"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "mask"), suffix=".png"),
)
PASCALS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "PASCAL-S"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "mask"), suffix=".png"),
)
SOD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "SOD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "SOD", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "SOD", "mask"), suffix=".png"),
)
DUTS_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE", "mask"), suffix=".png"),
)
DUTS_TR = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TR"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TR", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TR", "mask"), suffix=".png"),
)

rgb_sod_data = OrderedDict(
    {
        "PASCAL-S": PASCALS,
        "ECSSD": ECSSD,
        "HKU-IS": HKUIS,
        "DUT-OMRON": DUTOMRON,
        "DUTS-TE": DUTS_TE,
    }
)
