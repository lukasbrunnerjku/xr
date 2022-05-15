import cv2
import mediapipe as mp
from typing import Tuple
import numpy as np
import time


class BodyDetector:
    # https://google.github.io/mediapipe/solutions/pose.html

    def __init__(self):

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            model_complexity=0,
            static_image_mode=False,
            smooth_landmarks=True,
            enable_segmentation=False,
            smooth_segmentation=False, 
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def __call__(self, img, flip=True) -> Tuple[bool, np.ndarray]:

        if flip:
            img = cv2.flip(img, 1)
            
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        print(imgRGB.shape)
        self.results = self.pose.process(imgRGB)
        success = self.results.pose_landmarks is not None
        return success, img

    def findPose3D(self, draw=True, parse=True):

        if draw:
            self.mpDraw.plot_landmarks(
                self.results.pose_world_landmarks, 
                self.mpPose.POSE_CONNECTIONS
            )

        if parse:
            keypoints = self.results.pose_world_landmarks.landmark
            return [[kp.x, kp.y, kp.z] for kp in keypoints]

    def findPose2D(self, img, draw=True, parse=True):

        if draw:
            self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                        self.mpPose.POSE_CONNECTIONS)

        if parse:
            self.lmList = []
            
            for lm in self.results.pose_landmarks.landmark:
                h, w, _ = img.shape
                x, y = int(lm.x * w), int(lm.y * h)
                self.lmList.append([x, y])
            return self.lmList
        
        
def main(draw: bool = False, flip: bool = True):

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = BodyDetector()

    while cap.isOpened():
        success, img = cap.read()
        if not success: continue
        
        success, img = detector(img, flip)
        if not success: continue

        # detector.findPose2D(img, draw=False, parse=False)
        #kpts = detector.findPose3D(draw=False, parse=True)
        # print(kpts)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        print('fps:', str(int(fps)))

        if draw:
            cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                        (255, 0, 255), 3)
            cv2.imshow("", img)
            
        if cv2.waitKey(5) & 0xFF == 27:
            break
    
    cap.release()


if __name__ == "__main__":
    main()