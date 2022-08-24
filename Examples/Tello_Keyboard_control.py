from threading import Thread
from unicodedata import name
from Tello_Keyboard_module import KeyBoard
from djitellopy import tello
from time import sleep



class KeyBoard_Control(Thread):
    def __init__(self, drone):
        self.kp = KeyBoard()
        self.drone = drone

    def getKeyboardInput(self):
        lr , fb , ud, yv = 0 , 0  , 0 , 0
        speed = 50

        if self.kp.getKey("LEFT"): lr = - speed
        elif self.kp.getKey("RIGHT"): lr = speed


        if self.kp.getKey("UP"): fb =  speed
        elif self.kp.getKey("DOWN"): fb = - speed
        
        if self.kp.getKey("w"): ud =  speed
        elif self.kp.getKey("s"): ud = -speed

        
        if self.kp.getKey("a"): yv =  -speed
        elif self.kp.getKey("d"): yv = speed

        if self.kp.getKey("q"): self.drone.land()
        if self.kp.getKey("e"): self.drone.takeoff()

        return [lr , fb , ud, yv]
        
    def KeyBoardControl(self):
        print("starting keyboard control")
        while True:
            vals = self.getKeyboardInput()
            self.drone.send_rc_control(vals[0],vals[1],vals[2],vals[3])

if __name__ =='__main__':
    drone = tello.Tello()
    drone.connect()
    print("Battery:", drone.get_battery())

    kc = KeyBoard_Control(drone)

    thread = Thread(target=kc.KeyBoardControl)
    thread.start()

