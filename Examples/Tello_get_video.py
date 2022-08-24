from concurrent.futures import thread
from threading import Thread
from djitellopy import tello
import cv2
from time import sleep


class Video(Thread):

    def __init__(self,drone):
        self.drone = drone
        self.drone.streamon()

    def getVideo(self):
        "start video"
        while True:
            img = self.drone.get_frame_read().frame
            img = cv2.resize(img, (360,240))
            cv2.imshow("image", img)
            cv2.waitKey(1)


if __name__ =='__main__':
    drone = tello.Tello()
    drone.connect()
    print("Battery:", drone.get_battery())
    
    
    vid = Video(drone)
    
    thread = Thread(target=vid.getVideo)
    thread.start()
    
    