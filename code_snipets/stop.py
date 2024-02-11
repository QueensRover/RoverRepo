from turtle import right
from qset_lib import Rover, AngleReader
from time import sleep
import signal

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()
    rover.send_command(0, 0) 

if __name__ == "__main__":
    main()
