# models from https://github.com/alvareson/caffe_model_for_dace_detection

# import packages
import numpy as np
import cv2

min_confidence = 0.7
window_name = "Window"

# load SSD and ResNet network based caffe model for 300x300 dim imgs
net = cv2.dnn.readNetFromCaffe(
    "models/deploy.prototxt.txt", "models/res10_300x300_ssd_iter_140000.caffemodel")

# video stream initialization
# TODO replace with Video from Faces (30 FPS, 30 Sec total 900 Frames)
cap = cv2.VideoCapture('./videos/pexels-artem-podrez-6952256.mp4')
# cap = cv2.VideoCapture(0)  # uncomment to use the webcam
# get the video frames' width and height for proper saving of videos
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

dec_result_file = open("assignments/04/detectionresults.txt", "w")
dec_result_file.write("Detection Results: \n")

# TODO define face count per frame
right_dec_file = open("assignments/04/rightcountfacesperframe.txt", "r")
right_dec_lines = right_dec_file.readlines()
right_dec_lines = [line.rstrip() for line in right_dec_lines]

# total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
right_captured_result_frames = 0
frame_count = 0

test = open("assignments/04/results.txt", "w")


do_write_video = False
if do_write_video:
    out_video = cv2.VideoWriter('video_result.mp4', cv2.VideoWriter_fourcc(
        *'mp4v'), 30, (frame_width, frame_height))

cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# loop over video frames
while cap.isOpened():
    ret, frame = cap.read()
    if(frame_count < len(right_dec_lines)):
        if ret:
            detected_faces = 0
            # convert frame dimensions to a blob and 300x300 dim
            (height, width) = frame.shape[:2]
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0,
                                         (300, 300), (104.0, 177.0, 123.0))

            # pass the blob into dnn
            net.setInput(blob)
            detections = net.forward()

            # loop over the detections to extract specific confidence
            for i in range(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]

                # greater than the minimum confidence
                if confidence < min_confidence:
                    continue

                # compute the boxes (x, y)-coordinates
                box = detections[0, 0, i, 3:7] * \
                    np.array([width, height, width, height])
                (x1, y1, x2, y2) = box.astype("int")

                # draw the bounding box of the face along with the associated
                # probability
                text = "{:.2f}%".format(confidence * 100) + \
                    " ( " + str(y2-y1) + ", " + str(x2-x1) + " )"
                y = y1 - 10 if y1 - 10 > 10 else y1 + 10
                cv2.rectangle(frame, (x1, y1), (x2, y2),
                              (0, 0, 255), 2)
                cv2.putText(frame, text, (x1, y),
                            cv2.LINE_AA, 0.45, (0, 0, 255), 2)

                detected_faces = detected_faces+1
            if(detected_faces == int(right_dec_lines[frame_count])):
                right_captured_result_frames = right_captured_result_frames+1
            test.write(str(detected_faces) + "\n")
            # show the output frame
            cv2.imshow(window_name, frame)

            if do_write_video:
                out_video.write(frame)

            # if the `w` key was pressed, break from the loop
            if cv2.waitKey(1) == ord("q"):
                break
        else:
            break
        frame_count = frame_count+1
    else:
        print("Break by frame: " + str(frame_count))
        break

total_frames = frame_count
dec_result_file.write(str(right_captured_result_frames) + "/" + str(total_frames) +
                      " are captured correctly. This means an amount of " + str(right_captured_result_frames/total_frames*100) + "%")
dec_result_file.write(
    "\nThis is only correct if you haven't quit the program by yourself!")
dec_result_file.flush()
dec_result_file.close()

dec_result_file = open("assignments/04/detectionresults.txt", "r")
dec_result_file_content = dec_result_file.read()
print(dec_result_file_content)
dec_result_file.close()

test.flush()
test.close()

# stop capturing
cv2.destroyAllWindows()
cap.release()
