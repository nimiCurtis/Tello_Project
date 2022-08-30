import pygame

class KeyBoard():

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((400,400))

    def getKey(self,keyName):
        ans = False
        for eve in pygame.event.get(): pass
        keyInput = pygame.key.get_pressed()
        myKey = getattr(pygame, 'K_{}'.format(keyName))
        if keyInput[myKey]:
            ans = True
        pygame.display.update()

        return ans

def main():
    k = KeyBoard()
    print(k.getKey("KP_MINUS"))

if __name__ =='__main__':
    while True:
        main()