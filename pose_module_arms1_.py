import cv2
import mediapipe as mp
import time
import math
# import pyttsx3
import numpy as np
import pandas as pd


class poseDetector():
    def __init__(self, mode=False, upbody=False, smoothmark=True, detcon=0.5, trackcon=0.5):
        self.mode = mode
        self.upbody = upbody
        self.smoothmark = smoothmark
        self.detcon = detcon
        self.trackcon = trackcon
        # self.angle=angle
        # self.audio=audio
        self.mppose = mp.solutions.pose
        self.pose = self.mppose.Pose(self.mode, self.upbody,
                                     self.smoothmark, self.detcon, self.trackcon)
        self.mpdraw = mp.solutions.drawing_utils

    '''def data(self):
        datapd = []
        df = pd.DataFrame(datapd, columns=["count"])
        df.append([count])
        df.to_csv('count.csv')
    '''


    def findpose(self, img, Draw=True):

        imgrgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgrgb)
        print(self.results.pose_landmarks)
        if self.results.pose_landmarks:
            if Draw:
                self.mpdraw.draw_landmarks(img, self.results.pose_landmarks, self.mppose.POSE_CONNECTIONS)

        return img

    def getpos(self, img, Draw=True):
        self.lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id,lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmlist.append([id, cx, cy])
                if Draw:
                    cv2.circle(img, (cx, cy), 4, (0, 0, 0), cv2.FILLED)
        return self.lmlist

    '''
    def speak(self,audio):
        engine=pyttsx3.init('sapi5')
        voices=engine.getProperty('voices')
        #print(voices[1].id)
        engine.setProperty('voices',voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    '''

    def findangle(self, img, p1, p2, p3, Draw=True):
        # get the landmarks
        # _,x1,y1=self.lmlist[p1]
        x1, y1 = self.lmlist[p1][1:]
        x2, y2 = self.lmlist[p2][1:]
        x3, y3 = self.lmlist[p3][1:]
        # get the Angles
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) - math.atan2(y1 - y2, x1 - x2))
        if angle < 0:
            angle += 360

        cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 20), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        if Draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x2, y2), (x3, y3), (255, 255, 255), 3)

            cv2.circle(img, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), 2)
            cv2.circle(img, (x2, y2), 6, (255, 0, 255), cv2.FILLED)
            # cv2.circle(img,(x2,y2),15,(255,0,255),2
            cv2.circle(img, (x3, y3), 8, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 255), 2)
        '''    
        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            cv2.circle(img, (x1, y1), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x1, y1), 15, (0, 0, 255), 2)
            cv2.circle(img, (x2, y2), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (0, 0, 255), 2)
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (0, 0, 255), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        '''
        return angle


def main():
    # cap=cv2.VideoCapture(r"C:\Users\Annie_Unplugged\my\dataset\fingure\cv2module\pose_module\pose_sample2.mp4")
    cap = cv2.VideoCapture(0)
    # pertime=0
    detector = poseDetector()
    count = 0
    dir = 0
    # resize = cv2.resize(image, (640, 480))
    while True:
        success, img = cap.read()
        img = cv2.resize(img, (1200, 720))
        img = detector.findpose(img, False)
        lmlist = detector.getpos(img, Draw=False)

        if len(lmlist) != 0:
            # right arm
            # detector.findangle(img,16,14,12)
            # left arm
            detector.findangle(img, 11, 13, 15)

            angle = detector.findangle(img, 11, 13, 15)
            # # Left Arm
            # angle = detector.findangle(img, 11, 13, 15,False)
            per = np.interp(angle, (30, 150), (0, 100))
            bar = np.interp(angle, (30, 150), (650, 100))
            # print(angle, per)

            # Check for the dumbbell curls
            color = (0, 255, 0)
            if per == 100:
                color = (1, 190, 200)
                if dir == 0:
                    count += 0.5
                    dir = 1
            if per == 0:
                color = (1, 190, 200)
                if dir == 1:
                    count += 0.5
                    dir = 0
            print(count)

            # print(lmlist[1])
            # cv2.circle(img,(lmlist[14][2],lmlist[14][1]),4,(255,255,0),cv2.FILLED)
            # print(self.angle)
            # print(lmlist[13])
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1165, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1165, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)

            # Draw Curl Count
            cv2.rectangle(img, (0, 600), (150, 750), (0, 200, 200), cv2.FILLED)
            cv2.putText(img, str(int(count)), (15, 670), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 50, 255), 5)
            cv2.putText(img, str("Right arm"), (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        '''

            curtime=time.time()
            fps=1/(curtime-pertime)
            pertime=curtime
            cv2.putText(img,str(int(fps)),(70,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        '''
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()