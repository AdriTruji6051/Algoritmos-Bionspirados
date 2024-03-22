import keyboard
import time

DataPath = "Assets/Data/"
def recordMovements(key):
    file = open(DataPath + "Movements.txt", "a")
    file.write(key)
    file.close()
    
execute = True
while execute:
    print('INICIANDO')
    time.sleep(0)
    keyboard.press('W')
    recordMovements('W')
    print('W')
    
    time.sleep(0)
    keyboard.press('A')
    recordMovements('A')
    print('A')
    
    time.sleep(0)
    keyboard.press('S')
    recordMovements('S')
    print('S')
    
    time.sleep(0)
    keyboard.press('D')
    recordMovements('D')
    print('D')
    
    time.sleep(10)
    execute = False
