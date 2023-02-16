"""
    Functions to define ros2 element in the graphic context
"""
import cv2
import numpy as np

SIZE = (720, 1280, 3)
BG_FRAME = np.ones(SIZE, np.uint8) * 245
BORDER = [10, 10]
def create_node(name: str, origin: list, background: np.ndarray=None) -> np.ndarray:
    if background is None: background = BG_FRAME
    img = background.copy()

    # extract dimension
    (lbl_w, lbl_h), _ = cv2.getTextSize(name, fontScale=0.8, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, thickness=1)

    # text
    ap = [origin[0], origin[1] + lbl_h]
    img = cv2.putText(img, name, ap, fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(0, 0, 100))

    # ellipse
    center = [origin[0] + lbl_w // 2, origin[1] + lbl_h // 2]
    img = cv2.ellipse(img, center, (lbl_w // 2 + BORDER[0], lbl_h // 2 + BORDER[1]), angle=0, startAngle=0, endAngle=360, color=(0, 0, 0), thickness=1)
    return img