import cv2
import mediapipe as mp
import time


class HandDetector():
    # https://google.github.io/mediapipe/solutions/hands.html

    def __init__(self):

        self.mpDraw = mp.solutions.drawing_utils
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            model_complexity=0,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
        )

    def findHands(self, img, draw=True):

        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img
    
    def worldHands(self, img):
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgRGB.flags.writeable = False
        results = self.hands.process(imgRGB)
        if results.multi_hand_world_landmarks:
            print(results.multi_hand_world_landmarks)
            """
            [landmark {
            x: -0.013786965981125832
            y: 0.087281234562397
            z: 0.002671885071322322
            }
            landmark {
            x: 0.017654426395893097
            y: 0.06580586731433868
            z: -0.005411498714238405
            }....
            """
            import pdb; pdb.set_trace()

    def findPosition(self, img, handNo):

        lmList = []
        if self.results.multi_hand_landmarks:
            if handNo < len(self.results.multi_hand_landmarks):
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, lm in enumerate(myHand.landmark):
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                
        return lmList


def main(draw: bool = True):

    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    detector = HandDetector()

    while cap.isOpened():
        success, img = cap.read()

        if not success:
            continue

        detector.worldHands(img)

        # img = detector.findHands(img, draw=draw)

        # lmList0 = detector.findPosition(img, 0)
        # if len(lmList0) != 0:
        #     print('hand0:', lmList0[4])

        # lmList1 = detector.findPosition(img, 1)
        # if len(lmList1) != 0:
        #     print('hand1:', lmList1[4])
        
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