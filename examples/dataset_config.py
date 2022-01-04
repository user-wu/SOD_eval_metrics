# -*- coding: utf-8 -*-
import os

_RGB_SOD_ROOT = "D:\Projects\PYSoD_New\data\data_label"

DUT_OMRON = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUT-OMRON", "mask"), suffix=".png"),
)

ECSSD = dict(
    root=os.path.join(_RGB_SOD_ROOT, "ECSSD"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "ECSSD", "mask"), suffix=".png"),
)
HKU_IS = dict(
    root=os.path.join(_RGB_SOD_ROOT, "HKU-IS"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "image"), suffix=".png"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "HKU-IS", "mask"), suffix=".png"),
)
PASCAL_S = dict(
    root=os.path.join(_RGB_SOD_ROOT, "PASCAL-S"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "PASCAL-S", "mask"), suffix=".png"),
)

DUTS_TE = dict(
    root=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE"),
    image=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE", "image"), suffix=".jpg"),
    mask=dict(path=os.path.join(_RGB_SOD_ROOT, "DUTS/DUTS-TE", "mask"), suffix=".png"),
)
