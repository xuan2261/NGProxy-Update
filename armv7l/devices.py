#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_signal():
    """
    Just run python interpreter to catches the signal
    """
    return True


# VENDOR ID - MODEL ID - IFACE
VENDOR_MODEL_IFACE = {
    # ZTE
    '19d2': {
        '0117': 2,  # MF190
        '1544': 2,  # MF190J
        '0082': 2,  # MF190
        '0124': 2,  # MF110, MF190, MF656A, MF668A, MF669
        '0016': 2,  # MF190
        '0031': 3,  # MF110/MF627/MF636
        '2003': 3,  # MF190
        '0108': 3,  # MF190SVIED010000
        '2000': 2,  # MF627/MF628/MF628+/MF636+
    },
    # Huawei
    '12d1': {
        '1436': 0,  # Broadband stick
        '156b': 0,  # E3276s-151, E3251
        '156c': 0,  # E3276s-151, E3251
        '1506': 0,  # Modem Networkcard
        '14a8': 0,  # Huawei E173 (Viettel 3G)
    }
}
