import cv2
from flask import Flask, Response, request
import numpy
from cvzone.PoseModule import PoseDetector as pose
#use 0 to use camera of pc and 1 for external camera
cap = cv2.VideoCapture(0)
app = Flask(__name__)

def pushups():
    cap = cv2.VideoCapture(0)
    # .5 is defualt and increase it if detection is not accurate. it will increase power detection
    detector = pose(detectionCon=0.57)
    per = 0
    angle = 0
    dirr = 0
    sit = 0
    while True:
        _, img = cap.read()
        img = detector.findPose(img)
        llist, bbox = detector.findPosition(img, False)
        if llist:
            try:
                angle = detector.findAngle(img, 12, 14, 16)
                # print(angle)
                per = numpy.interp(angle, (35, 170), (100, 0))
                barlevel = numpy.interp(angle, (35, 170), (70, 400))
                cv2.rectangle(img, (600, int(barlevel)), (600 + 30, 200 + 200), (200, 100, 0), cv2.FILLED)
                cv2.rectangle(img, (600, 100), (600 + 30, 200 + 200), (), 4)
                # 180stand to 40sit
                if per >= 60:
                    if dirr == 0:
                        sit += 0.5
                        dirr = 1
                if per == 0:
                    if dirr == 1:
                        sit += 0.5
                        dirr = 0
                cv2.rectangle(img, (220, 50), (20, 5), (255, 100, 0), cv2.FILLED)
                cv2.putText(img, f"Total Reps:{str(int(sit))}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                            2)

            except Exception as e:
                pass
        _, frame = cv2.imencode('.JPEG', img)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')


def runn():
    detector = pose(detectionCon=0.57)
    per = 0
    angle = 0
    dirr = 0
    sit = 0

    while True:
        _, img = cap.read()
        img = detector.findPose(img)
        llist, bbox = detector.findPosition(img, False)

        if llist:
            try:
                angle = detector.findAngle(img, 24, 26, 28)
                # print(angle)
                per = numpy.interp(angle, (35, 170), (100, 0))
                barlevel = numpy.interp(angle, (35, 170), (70, 400))

                cv2.rectangle(img, (600, int(barlevel)), (600 + 30, 200 + 200), (200, 100, 0), cv2.FILLED)
                cv2.rectangle(img, (600, 100), (600 + 30, 200 + 200), (), 4)

                # 180stand to 40sit
                if per >= 79:
                    if dirr == 0:
                        sit += 0.5
                        dirr = 1
                if per == 0:
                    if dirr == 1:
                        sit += 0.5
                        dirr = 0
                cv2.rectangle(img, (220, 50), (20, 5), (255, 100, 0), cv2.FILLED)
                cv2.putText(img, f"Total Reps:{str(int(sit))}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255),
                            2)

            except Exception as e:
                pass

        _, frame = cv2.imencode('.JPEG', img)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame.tobytes() + b'\r\n')


@app.route('/')
def squat():
    return """    <form action="/sq" method="get">
    <table border="9" >
        <tr><td><input type="submit" name="sub" style="color:#1a2421;background-color:#cbcbcb;font-size: 20px;text-align:center;height:40px;width:90px" value="Squats"><input type="submit" name="sub" style="color:#1a2421;background-color:#cbcbcb;font-size: 20px;text-align:center;height:40px;width:90px" value="pushups"></td></tr>

    </table>
        </form>"""
# def push_ups():
#     return
@app.route('/sq')
def col():
    a = request.args.get('sub')
    if a == "Squats":
        return Response(runn(), mimetype='multipart/x-mixed-replace; boundary=frame')
    elif a=="pushups":
        return Response(pushups(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Invalid request"


if __name__ == '__main__':
    app.run(debug=False)
