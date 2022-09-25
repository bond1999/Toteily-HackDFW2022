import cv2
import numpy as np
from pyzbar.pyzbar import decode
import customer as cust
from time import gmtime, strftime, localtime


def stream(allCustomers):

    displaying_text = False

    capture = cv2.VideoCapture(0)
    previous_frame = None
    first = ""
    last = ""
    id = None
    entered = None
    timer = 0

    cv2.namedWindow("Tote-aly")
    cv2.moveWindow("Tote-aly", 300, 10)

    while True:
        timer += 1
        ret, frame = capture.read()
        if ret:
            frame = cv2.resize(frame, (1280, 960))
            if previous_frame is None:
                previous_frame = frame
            diff = cv2.absdiff(previous_frame, frame)

            if np.sum(diff) > 0:
                for qr in decode(frame):
                    if qr:
                        timer = 0
                        uuid = qr.data.decode("utf-8")
                        print(uuid)
                        points = np.array([qr.polygon], np.int32)
                        points = points.reshape((-1, 1, 2))
                        cv2.polylines(frame, [points], True, (0, 255, 0), 15)

                        for c in allCustomers:
                            if c.uuid == uuid:
                                new_customer = c
                                first = c.first_name
                                last = c.last_name
                                id = c.uuid
                                displaying_text = True
                                found_customer = True
                                new_customer.time_entered = strftime("%Y-%m-%d %H:%M:%S", localtime())
                                entered = new_customer.time_entered

            if timer == 45:
                displaying_text = False
            previous_frame = frame

            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 1.5
            color = (0, 255, 0)
            thickness = 3

            if displaying_text:
                frame = cv2.putText(frame, "UUID: " + id, (25, 825), font,
                                    font_scale, (0, 0, 0), 5, cv2.LINE_AA)
                frame = cv2.putText(frame, "UUID: " + id, (25, 825), font,
                                    font_scale, color, thickness, cv2.LINE_AA)

                frame = cv2.putText(frame, first + " " + last, (25, 875), font,
                                    font_scale, (0, 0, 0), 5, cv2.LINE_AA)
                frame = cv2.putText(frame, first + " " + last, (25, 875), font,
                                    font_scale, color, thickness, cv2.LINE_AA)

                frame = cv2.putText(frame, entered, (25, 925), font,
                                    font_scale, (0, 0, 0), 5, cv2.LINE_AA)
                frame = cv2.putText(frame, entered, (25, 925), font,
                                    font_scale, color, thickness, cv2.LINE_AA)

            cv2.imshow("Tote-ily", frame)
            cv2.waitKey(1)
        else:
            break
