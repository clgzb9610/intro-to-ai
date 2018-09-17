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

def readLeftAndRight(robot):
    robot.turnLeft(0.2, 0.2)
    leftVal = robot.readUltra()
    robot.turnRight(0.2, 0.4)
    rightVal = robot.readUltra()
    robot.turnLeft(0.2, 0.2)
    return leftVal, rightVal


bttn = ev3.Button()
while not bttn.any():
    myBot.forward(1.0)
    leftDist, rightDist = readLeftAndRight(myBot)
    leftSpeed = convertDistToSpeed(leftDist)
    rightSpeed = convertDistToSpeed(rightDist)
    myBot.curve(leftSpeed, 0.3)
    myBot.curve(0.3, rightSpeed)

myBot.stop()