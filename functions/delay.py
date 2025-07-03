from time import sleep

def Delay(value):
    while not value <= 1:
        value -= 0.123
        print(
            f'\x1b[1;39m[\x1b[1;36mANHCODE\x1b[1;39m][ \x1b[1;36mDELAY \x1b[1;39m][\x1b[1;36m{str(value)[0:5]}\x1b[1;39m][\x1b[1;33mX  \x1b[1;39m ]', '               ', end='\r')
        sleep(0.025)
        print(
            f'\x1b[1;39m[\x1b[1;36mANHCODE\x1b[1;39m][ \x1b[1;36mDELAY \x1b[1;39m][\x1b[1;36m{str(value)[0:5]}\x1b[1;39m[\x1b[1;33m X   \x1b[1;39m]', '               ', end='\r')
        sleep(0.025)
        print(
            f'\x1b[1;39m[\x1b[1;36mANHCODE\x1b[1;39m][ \x1b[1;36mDELAY \x1b[1;39m][\x1b[1;36m{str(value)[0:5]}\x1b[1;39m[\x1b[1;33m  X  \x1b[1;39m]', '               ', end='\r')
        sleep(0.025)
        print(
            f'\x1b[1;39m[\x1b[1;36mANHCODE\x1b[1;39m][ \x1b[1;36mDELAY \x1b[1;39m][\x1b[1;36m{str(value)[0:5]}\x1b[1;39m[\x1b[1;33m   X \x1b[1;39m]', '               ', end='\r')
        sleep(0.025)
        print(
            f'\x1b[1;39m[\x1b[1;36mANHCODE\x1b[1;39m][ \x1b[1;36mDELAY \x1b[1;39m][\x1b[1;36m{str(value)[0:5]}\x1b[1;39m[\x1b[1;33m    X\x1b[1;39m]', '               ', end='\r')
        sleep(0.025)
