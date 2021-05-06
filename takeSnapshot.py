import cv2

def takeSnapshot():
    videoCapture=cv2.VideoCapture(1)
    result=True
    while(result):
        ret,frame=videoCapture.read()
        cv2.imwrite("picture1.mp4",frame)
        result=False

    videoCapture.release()
    cv2.destroyAllWindows()

takeSnapshot()