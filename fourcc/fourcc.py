def decode_fourcc(cc):
    """convert fourcc number to str"""
    return "".join([chr((int(cc) >> 8 * i) & 0xFF) for i in range(4)])

import cv2

vc = cv2.VideoCapture('./demo_ot_vp80.webm')
print(decode_fourcc(vc.get(cv2.CAP_PROP_FOURCC)))
