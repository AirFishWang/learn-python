# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     play_video
   Description :
   Author :        wangchun
   date：          18-11-15
-------------------------------------------------
   Change Activity:
                   18-11-15:
-------------------------------------------------
"""
import os
import cv2


def play_video(video_file):
    index = 2280
    cap = cv2.VideoCapture(video_file)
    fps = cap.get(cv2.CAP_PROP_FPS)
    length = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_index = 0

    while_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()

        if frame is None:
            print "Process {} frame is None, quit".format(os.getpid())
            break

        print "frame_index = {}".format(frame_index)

        if frame_index == index:
        # display
            while_frame = frame
            frame = cv2.resize(frame, (640, 360))
            cv2.imshow(os.path.split(video_file)[1], frame)
            k = cv2.waitKey(1)
            if k == ord('q'):
                break
            break

        frame_index += 1
        # print frame_index

    print "fps = {}".format(fps)
    print "length = {}".format(length)


    cap.set(cv2.CAP_PROP_POS_FRAMES, index*2)
    ret, frame = cap.read()
    print (while_frame - frame).any()

    frame = cv2.resize(frame, (640, 360))
    cv2.imshow("4560", frame)
    cv2.waitKey(0)
    # exit()



    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_file = "/home/wangchun/Desktop/ch01_201805130801160_0_0do1.mp4"
    # video_file = "/home/wangchun/Desktop/ch01_201805130738540_19_5do.mp4"
    play_video(video_file)