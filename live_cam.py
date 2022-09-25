import cv2
import numpy as np
from pyzbar.pyzbar import decode
import customer as cust
from time import gmtime, strftime

customers = []
displaying_text = False

# Entering Aisle Loop
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
previous_frame = None
# Move this inside the while loop for flashing
first = ""
last = ""
id = None
entered = None
timer = 0

# 640x480
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
                    found_customer = False

                    for c in customers:
                        if c.uuid == uuid:
                            first = c.first_name
                            last = c.last_name
                            id = c.uuid
                            entered = c.time_entered
                            displaying_text = True
                            found_customer = True

                    if not found_customer:
                        displaying_text = True
                        new_customer = cust.Customer(np.zeros(7))
                        new_customer.uuid = uuid
                        first = new_customer.first_name
                        last = new_customer.last_name
                        id = new_customer.uuid
                        entered = new_customer.time_entered
                        new_customer.time_entered = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                        customers.append(new_customer)


        if timer == 45:
            displaying_text = False
        previous_frame = frame

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 2
        color = (0, 255, 0)
        thickness = 7

        if displaying_text:
            frame = cv2.putText(frame, "UUID: " + id, (50, 850), font,
                                font_scale, (0, 0, 0), 18, cv2.LINE_AA)
            frame = cv2.putText(frame, "UUID: " + id, (50, 850), font,
                                font_scale, color, thickness, cv2.LINE_AA)

            frame = cv2.putText(frame, first + " " + last, (50, 925), font,
                                font_scale, (0, 0, 0), 18, cv2.LINE_AA)
            frame = cv2.putText(frame, first + " " + last, (50, 925), font,
                                font_scale, color, thickness, cv2.LINE_AA)

            frame = cv2.putText(frame, entered, (50, 1000), font,
                                font_scale, (0, 0, 0), 18, cv2.LINE_AA)
            frame = cv2.putText(frame, entered, (50, 1000), font,
                                font_scale, color, thickness, cv2.LINE_AA)


        cv2.imshow("Tote-aly", frame)
        cv2.waitKey(1)
        # out.write(frame)
    else:
        break