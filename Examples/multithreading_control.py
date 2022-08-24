from threading import Thread
from djitellopy import tello
from Tello_Keyboard_control import KeyBoard_Control
from Tello_get_video import Video 


if __name__ == '__main__':

    drone = tello.Tello()
    drone.connect()
    print(drone.get_battery())
    drone.streamon()

    vid = Video(drone)
    kc = KeyBoard_Control(drone)

    th1 = Thread(target=vid.getVideo)
    th2 = Thread(target=kc.KeyBoardControl)

    th1.start()
    th2.start()

