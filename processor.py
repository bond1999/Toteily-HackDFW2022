import cv2
import numpy as np
from pyzbar.pyzbar import decode

"""
Notes:
- 3840x2160 -> 1920x1080
- QR code detection is computationally expensive
    - Only try to detect a QR code if there is a significant change in the frame
"""


def process():

    capture = cv2.VideoCapture("resources/vision/qr_walk_resized.mp4")
    previous_frame = None
    while True:
        ret, frame = capture.read()
        if ret:

            if previous_frame is None:
                previous_frame = frame

            diff = cv2.absdiff(previous_frame, frame)

            # 60,000,000
            if np.sum(diff) > 60000000:
                # print(np.sum(diff))

                for qr in decode(frame):
                    if qr:
                        uuid = qr.data.decode("utf-8")
                        print(uuid)
                        points = np.array([qr.polygon], np.int32)
                        points = points.reshape((-1, 1, 2))
                        cv2.polylines(frame, [points], True, (0, 255, 0), 15)

            previous_frame = frame

            cv2.imshow("Tote-aly", frame)
            cv2.waitKey(1)
        else:
            break


process()
