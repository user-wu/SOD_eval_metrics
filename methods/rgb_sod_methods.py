# -*- coding: utf-8 -*-
import os
from collections import OrderedDict

from configs.utils.config_generator import curve_info_generator, simple_info_generator

_RGBSOD_METHODS_ROOT = "D:\Projects\PySODMetrics\data\experience_result"
_RGBSOD_DATASET_NAMES = ["PASCAL-S", "ECSSD", "HKU-IS", "DUT-OMRON", "DUTS-TE", "SOD"]

_METHODS_DIR_NAMES = {
    "BASNet": "BASNet",
    "PoolNet": "PoolNet",
    "AFNet": "AFNet",
    "CAGNet": "CAGNet",
    "EGNet": "EGNet",
    "GateNet": "GateNet",
    "GCPANet": "GCPANet",
    "MINet": "MINet",
    # "PAKRNet_2021_aaai": "PAKRN",
    # "PFANet_2021_aaai": "PFANet",
    # "SGLKRN_2021_aaai": "SGLKRN",
    # "U2NET_2020_PattenRecognition": "U2Net",
    # "LDFNet_2020_cvpr":"LDFNet",
    "DFINet":"DFINet",
    "MLMSNet":"MLMSNet",
    "F3Net": "F3Net",
    "Ours":"Ours",

}


BASNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["BASNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


PoolNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PoolNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}



AFNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["AFNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


CAGNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["CAGNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}

EGNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["EGNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


GateNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GateNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}




GCPANet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["GCPANet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}

MINet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MINet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}
#
# PAKRNet_2021_aaai = {
#     "PASCAL-S": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[0]
#         ),
#         suffix=".png",
#     ),
#     "ECSSD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[1]
#         ),
#         suffix=".png",
#     ),
#     "HKU-IS": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[2]
#         ),
#         suffix=".png",
#     ),
#     "DUT-OMRON": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[3]
#         ),
#         suffix=".png",
#     ),
#     "DUTS-TE": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[4]
#         ),
#         suffix=".png",
#     ),
#     "SOD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PAKRNet_2021_aaai"], _RGBSOD_DATASET_NAMES[5]
#         ),
#         suffix=".png",
#     ),
# }
#
# PFANet_2021_aaai = {
#     "PASCAL-S": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[0]
#         ),
#         suffix=".png",
#     ),
#     "ECSSD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[1]
#         ),
#         suffix=".png",
#     ),
#     "HKU-IS": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[2]
#         ),
#         suffix=".png",
#     ),
#     "DUT-OMRON": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[3]
#         ),
#         suffix=".png",
#     ),
#     "DUTS-TE": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[4]
#         ),
#         suffix=".png",
#     ),
#     "SOD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["PFANet_2021_aaai"], _RGBSOD_DATASET_NAMES[5]
#         ),
#         suffix=".png",
#     ),
# }
#
#
# SGLKRN_2021_aaai = {
#     "PASCAL-S": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[0]
#         ),
#         suffix=".png",
#     ),
#     "ECSSD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[1]
#         ),
#         suffix=".png",
#     ),
#     "HKU-IS": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[2]
#         ),
#         suffix=".png",
#     ),
#     "DUT-OMRON": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[3]
#         ),
#         suffix=".png",
#     ),
#     "DUTS-TE": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[4]
#         ),
#         suffix=".png",
#     ),
#     "SOD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["SGLKRN_2021_aaai"], _RGBSOD_DATASET_NAMES[5]
#         ),
#         suffix=".png",
#     ),
# }
#
#
# U2NET_2020_PattenRecognition = {
#     "PASCAL-S": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[0]
#         ),
#         suffix=".png",
#     ),
#     "ECSSD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[1]
#         ),
#         suffix=".png",
#     ),
#     "HKU-IS": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[2]
#         ),
#         suffix=".png",
#     ),
#     "DUT-OMRON": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[3]
#         ),
#         suffix=".png",
#     ),
#     "DUTS-TE": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[4]
#         ),
#         suffix=".png",
#     ),
#     "SOD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["U2NET_2020_PattenRecognition"], _RGBSOD_DATASET_NAMES[5]
#         ),
#         suffix=".png",
#     ),
# }


# LDFNet_2020_cvpr = {
#     "PASCAL-S": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[0]
#         ),
#         suffix=".png",
#     ),
#     "ECSSD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[1]
#         ),
#         suffix=".png",
#     ),
#     "HKU-IS": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[2]
#         ),
#         suffix=".png",
#     ),
#     "DUT-OMRON": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[3]
#         ),
#         suffix=".png",
#     ),
#     "DUTS-TE": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[4]
#         ),
#         suffix=".png",
#     ),
#     "SOD": dict(
#         path=os.path.join(
#             _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["LDFNet_2020_cvpr"], _RGBSOD_DATASET_NAMES[5]
#         ),
#         suffix=".png",
#     ),
# }


DFINet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["DFINet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


MLMSNet = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["MLMSNet"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


F3Net = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["F3Net"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}


Ours = {
    "PASCAL-S": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[0]
        ),
        suffix=".png",
    ),
    "ECSSD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[1]
        ),
        suffix=".png",
    ),
    "HKU-IS": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[2]
        ),
        suffix=".png",
    ),
    "DUT-OMRON": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[3]
        ),
        suffix=".png",
    ),
    "DUTS-TE": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[4]
        ),
        suffix=".png",
    ),
    "SOD": dict(
        path=os.path.join(
            _RGBSOD_METHODS_ROOT, _METHODS_DIR_NAMES["Ours"], _RGBSOD_DATASET_NAMES[5]
        ),
        suffix=".png",
    ),
}




curve_info = curve_info_generator()
methods_info_for_drawing = OrderedDict(
    {
        "BASNet": curve_info(BASNet, "BASNet"),
        "PoolNet": curve_info(PoolNet, "PoolNet"),
        "AFNet": curve_info(AFNet, "AFNet"),
        "CAGNet": curve_info(CAGNet, "CAGNet"),
        "EGNet": curve_info(EGNet, "EGNet"),
        "GateNet": curve_info(GateNet, "GateNet"),
        "GCPANet": curve_info(GCPANet, "GCPANet"),
        "MINet": curve_info(MINet, "MINet"),
        # "PAKRNet_2021_aaai": curve_info(PAKRNet_2021_aaai, "PAKRNet_2021_aaai"),
        # "PFANet_2021_aaai": curve_info(PFANet_2021_aaai, "PFANet_2021_aaai"),
        # "SGLKRN_2021_aaai": curve_info(SGLKRN_2021_aaai, "SGLKRN_2021_aaai"),
        # "U2NET_2020_PattenRecognition": curve_info(U2NET_2020_PattenRecognition, "U2NET_2020_PattenRecognition"),
        # "LDFNet_2020_cvpr": curve_info(LDFNet_2020_cvpr, "LDFNet_2020_cvpr"),
        "DFINet": curve_info(DFINet, "DFINet"),
        "MLMSNet": curve_info(MLMSNet, "MLMSNet"),
        "F3Net": curve_info(F3Net, "F3Net"),
        "Ours": curve_info(Ours, "Ours"),
    }
)
simple_info = simple_info_generator()


methods_info_for_selecting = OrderedDict(
    {
        "BASNet": simple_info(BASNet, "BASNet"),
        "PoolNet": simple_info(PoolNet, "PoolNet"),
        "AFNet": simple_info(AFNet, "AFNet"),
        "EGNet": simple_info(EGNet, "EGNet"),
        "GateNet": simple_info(GateNet, "GateNet"),
        "GCPANet": simple_info(GCPANet, "GCPANet"),
        "MINet": simple_info(MINet, "MINet"),
        # "PAKRNet_2021_aaai": simple_info(PAKRNet_2021_aaai, "PAKRNet_2021_aaai"),
        # "PFANet_2021_aaai": simple_info(PFANet_2021_aaai, "PFANet_2021_aaai"),
        # "SGLKRN_2021_aaai": simple_info(SGLKRN_2021_aaai, "SGLKRN_2021_aaai"),
        # "U2NET_2020_PattenRecognition": simple_info(U2NET_2020_PattenRecognition, "U2NET_2020_PattenRecognition"),
        # "LDFNet_2020_cvpr": simple_info(LDFNet_2020_cvpr, "LDFNet_2020_cvpr"),
        "DFINet": simple_info(DFINet, "DFINet"),
        "MLMSNet": simple_info(MLMSNet, "MLMSNet"),
        "F3Net": simple_info(F3Net, "F3Net"),
        "Ours": simple_info(Ours, "Ours"),
    }
)

