import ev3dev.ev3 as ev3
from basicBot import BasicBot

myBot = BasicBot("Loki")
myBot.setGyroSensor('in1')
myBot.setColorSensor('in3')
myBot.setUltrasonicSensor('in4')

# myBot.setMotorPort('leftMotor', 'outB')
# myBot.setMotorPort('rightMotor', 'outD')

def convertDistToSpeed(distance):
    if distance > 25:
        return 1
    else:
        return (distance - 25) / 25.0


bttn = ev3.Button()
while not bttn.any():
    speed = convertDistToSpeed(myBot.readUltra())
    myBot.forward(speed)

myBot.stop()