from qset_lib import Rover, AngleReader
from time import sleep
import signal
import math

#This hsould only be the function branch

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)
    i = 0

    gpsX = 10
    gpsY = 5
    initialAngle = math.atan2(abs(gpsY),abs(gpsX)) *(180 / math.pi)
    dx = gpsX - rover.x
    dy = gpsY - rover.y
    angle = math.atan2(abs(dy),abs(dx)) *(180 / math.pi) 

        

    left_side_speed = 1
    right_side_speed = 1
    isTooClose = False
    firstQuad = False
    secondQuad = False
    thirdQuad = False
    fourthQuad = False
    try:
        while not isTooClose or True:
            print(" ANGLE: " + str(angle_reader.read_angle))
            # this line prints the current location and heading of the rover
            print("X: " + str(rover.x) + " Y: " + str(rover.y) + " Heading: " + str(rover.heading))
            # the below lines iterate through all the laser scan lines and prints if the distance is less than 0.5 meters

            if(gpsX > 0 and gpsY > 0):
                firstQuad = True
            if(gpsX > 0 and gpsY < 0):
                fourthQuad = True
            if(gpsX < 0 and gpsY < 0):
                thirdQuad = True
            if(gpsX < 0 and gpsY > 0):
                secondQuad = True



            if firstQuad:
                print(initialAngle)
                angle = math.atan2(abs(dy),abs(dx)) *(180 / math.pi) 
                headingDirection = angle-90
                if rover.heading > initialAngle-90:
                    while rover.heading > headingDirection:
                        left_side_speed = 1
                        right_side_speed = -1
                        rover.send_command(left_side_speed, right_side_speed)
                else:
                    while rover.heading < headingDirection:
                        left_side_speed = -1
                        right_side_speed = 1
                        rover.send_command(left_side_speed, right_side_speed)


            if fourthQuad:
                angle = math.atan2(abs(dy),abs(dx)) *(180 / math.pi) 
                headingDirection = -90-angle
                if rover.heading > -90-initialAngle:
                    while rover.heading > headingDirection:
                        left_side_speed = 1
                        right_side_speed = -1
                        rover.send_command(left_side_speed, right_side_speed)
                else:
                    while rover.heading < headingDirection:
                        left_side_speed = -1
                        right_side_speed = 1
                        rover.send_command(left_side_speed, right_side_speed)



            if thirdQuad:
                angle = math.atan2(abs(dy),abs(dx)) *(180 / math.pi) 
                headingDirection = angle+90
                if rover.heading < initialAngle+90:
                    while rover.heading < headingDirection:
                        left_side_speed = -1
                        right_side_speed = 1
                        rover.send_command(left_side_speed, right_side_speed)
                else:
                    while rover.heading > headingDirection:
                        left_side_speed = 1
                        right_side_speed = -1
                        rover.send_command(left_side_speed, right_side_speed)


            if secondQuad:
                angle = math.atan2(abs(dy),abs(dx)) *(180 / math.pi) 
                headingDirection = 90-angle
                if rover.heading < 90-initialAngle:
                    while rover.heading < headingDirection:
                        left_side_speed = -1
                        right_side_speed = 1
                        rover.send_command(left_side_speed, right_side_speed)
                else:
                    while rover.heading > headingDirection:
                        left_side_speed = 1
                        right_side_speed = -1
                        rover.send_command(left_side_speed, right_side_speed)
            
            left_side_speed = 5
            right_side_speed = 5
            rover.send_command(left_side_speed,right_side_speed)


            for dist in rover.laser_distances:
                if dist < 5:
                    print("TOO CLOSE")
                    left_side_speed = 0
                    right_side_speed = 0
                    break
            # the below line sends a command to the rover (simulation) 
            rover.send_command(left_side_speed, right_side_speed)
            i = i + 1
            sleep(0.01)

    except KeyboardInterrupt:
        pass

    rover.send_command(0, 0)

if __name__ == "__main__":
    main()