import ev3dev.ev3 as ev3
from basicBot import BasicBot

myBot = BasicBot("Loki")
myBot.setGyroSensor('in1')
myBot.setColorSensor('in3')
myBot.setUltrasonicSensor('in4')

# myBot.setMotorPort('leftMotor', 'outB')
# myBot.setMotorPort('rightMotor', 'outD')

def convertDistToSpeed(distance):
    if distance > 100:
        return 1
    else:
        return (distance - 50) /50


bttn = ev3.Button()
while not bttn.any():
    print(myBot.readUltra())
    speed = convertDistToSpeed(myBot.readUltra())
    print(speed)
    myBot.forward(speed)
