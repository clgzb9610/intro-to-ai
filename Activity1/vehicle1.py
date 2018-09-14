import ev3dev.ev3 as ev3
from basicBot import BasicBot

myBot = BasicBot("Loki")
myBot.setGyroSensor('in1')
myBot.setColorSensor('in3')
myBot.setUltrasonicSensor('in4')

myBot.setMotorPort('outC')
rightM = ev3.LargeMotor('outB')