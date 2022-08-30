from concurrent.futures import thread
from threading import Thread
from djitellopy import tello
import cv2
from time import sleep


class Video():

    def __init__(self,drone):
        self.drone = drone
        self.drone.streamon()
        self.resolution = [360,240]

    def getVideo(self):
        "start video"
        org = [10, self.resolution[1]-20]
        font = cv2.FONT_HERSHEY_SIMPLEX
        fontScale = 0.4
        # Blue color in BGR
        color = (255, 0, 0)
        thickness = 1
        text=''
        while True:
            text = "Speed X: " + str(self.drone.get_speed_x()) + "\nBattery: " + str(self.drone.get_battery())
            
            img = self.drone.get_frame_read().frame
            img = cv2.resize(img, (self.resolution[0],self.resolution[1]))
            
            # Using cv2.putText() method
            dy =  12
            for i, line in enumerate(text.split('\n')):
                y = org[1] + i*dy
                cv2.putText(img, line, (org[0],y), font, 
                   fontScale, color, thickness, cv2.LINE_AA)
            
            cv2.imshow("image", img)
            cv2.waitKey(1)


if __name__ =='__main__':
    drone = tello.Tello()
    drone.connect()
    
    vid = Video(drone)
    vid.getVideo()

    
    