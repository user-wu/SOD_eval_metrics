# -*- coding: utf-8 -*-
from .datasets.rgb_sod import rgb_sod_data
from .methods import (
    rgb_sod_methods,
)

total_info = dict(
    rgb_sod=dict(
        dataset=rgb_sod_data,
        method=dict(
            drawing=rgb_sod_methods.methods_info_for_drawing,
            selecting=rgb_sod_methods.methods_info_for_selecting,
        ),
    ),
)
