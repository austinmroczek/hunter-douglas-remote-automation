from gpiozero import LED
from time import sleep

Button1 = LED(4, active_high=False)
ButtonDown = LED(6, active_high=False)
ButtonUp = LED(5, active_high=False)

def setup():
  Button1.off()
  ButtonDown.off()
  ButtonUp.off()

def Group1Down(): # tell Group1 to go down using Radio Control
  # activate group 1
  Button1.on()
  sleep(1)
  Button1.off()
  sleep(1)
  ButtonDown.on()
  sleep(2)
  ButtonDown.off()
  sleep(1)
  
def Group1Up(): # tell Group1 to go Up using Radio Control
  # activate group 1
  Button1.on()
  sleep(1)
  Button1.off()
  sleep(1)
  ButtonUp.on()
  sleep(2)
  ButtonUp.off()
  sleep(1)



def run():
    Group1Up()
    Group1Down()
    


run()