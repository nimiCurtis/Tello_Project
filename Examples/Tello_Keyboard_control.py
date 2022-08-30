from threading import Thread
from unicodedata import name
from Tello_Keyboard_module import KeyBoard
from djitellopy import tello
from time import sleep



class KeyBoard_Control():
    def __init__(self, drone, speed=50):
        self.kp = KeyBoard()
        self.drone = drone
        self.speed = speed

    def getKeyboardInput(self):
        lr , fb , ud, yv = 0 , 0  , 0 , 0
        

        if self.kp.getKey("LEFT"): lr = - self.speed
        elif self.kp.getKey("RIGHT"): lr = self.speed


        if self.kp.getKey("UP"): fb =  self.speed
        elif self.kp.getKey("DOWN"): fb = - self.speed
        
        if self.kp.getKey("w"): ud =  self.speed
        elif self.kp.getKey("s"): ud = -self.speed

        
        if self.kp.getKey("a"): yv =  -self.speed
        elif self.kp.getKey("d"): yv = self.speed


        if self.kp.getKey("KP_PLUS"): 
            if self.speed<100:
                self.speed+=1
                print(f"speed increased to {self.speed}")
            else:
                self.speed = 100
                print(f"speed is 100 , can't be higher")
        elif self.kp.getKey("KP_MINUS"): 
            if self.speed>0: 
                self.speed-=1
                print(f"speed decreased to {self.speed}")
            else : 
                self.speed = 0
                print(f"speed is 0 , can't be lower")

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

