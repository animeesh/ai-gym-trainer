from flask import Flask, render_template, Response
import cv2
from pose_module_arms1_ import poseDetector
import numpy as np
#import time
import pandas as pd
#import pose_module_arms_
#import os
app = Flask(__name__)


def leftarm():
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
            per = np.interp(angle, (170,330), (0, 100))
            bar = np.interp(angle, (30, 150), (650, 100))
            print(angle, per)


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
            cv2.putText(img, str("Left arm"), (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', img)
            img = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result

        # cv2.imshow("image",img)
def rightarm():
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
            detector.findangle(img, 16, 14, 12)

            angle = detector.findangle(img, 16, 14, 12)
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

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', img)
            img = buffer.tobytes()
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result

def Pushup():
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
            detector.findangle(img, 16, 14, 12)

            angle = detector.findangle(img, 16, 14, 12)
            angle =detector.findangle(img, 15, 13, 11)
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

            dummy=[]
            path = "/Users/vinayvishwakarma/PycharmProjects/pythonProject/venv"
            dummy.append(count)
            #print(dummy)
            df=pd.DataFrame(dummy)
            df.to_csv(path,'filename.csv',index=False)


            # print(lmlist[1])
            # cv2.circle(img,(lmlist[14][2],lmlist[14][1]),4,(255,255,0),cv2.FILLED)
            # print(self.angle)
            # print(lmlist[13])
            # Draw Bar
            cv2.rectangle(img, (1100, 100), (1165, 650), color, 3)
            cv2.rectangle(img, (1100, int(bar)), (1165, 650), color, cv2.FILLED)
            cv2.putText(img, f'{int(per)} %', (1100, 75), cv2.FONT_HERSHEY_PLAIN, 4,
                        color, 4)
            '''
            data=[]
            df=pd.DataFrame(data,columns=["count"])
            df.to_csv('count.csv')
            '''


            # Draw Curl Count
            cv2.rectangle(img, (0, 600), (150, 750), (0, 200, 200), cv2.FILLED)
            cv2.putText(img, str(int(count)), (15, 670), cv2.FONT_HERSHEY_PLAIN, 5,
                        (0, 50, 255), 5)
            cv2.putText(img, str(" Pushups "), (70, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', img)
            img = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + img + b'\r\n')  # concat frame one by one and show result




@app.route('/')
def hello():
    # return "animesh"
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    # return "animesh"
    return render_template('camera.html')



@app.route('/video_feed1',methods=['POST'])
def video_feed1():
    return Response(leftarm(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed2',methods=['POST'])
def video_feed2():
    return Response(rightarm(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed3',methods=['POST'])
def video_feed3():
    return Response(Pushup(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/diet',methods=['POST'])
def diet():
    return render_template('diet.html')


if __name__ == '__main__':
    # app.config['TEMPLATES_AUTO_RELOAD']=True
    app.run()
