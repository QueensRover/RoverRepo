from qset_lib import Rover, AngleReader
from time import sleep
import signal
import math

def main():
    rover = Rover() # this line starts the connection to the rover and gives access to the rover data
    angle_reader = AngleReader()

    # This line allows for the KeyboardInterrupt to worl
    signal.signal(signal.SIGINT, signal.default_int_handler)

    while True:
        print("STOP THE ROVER")
        rover.send_command(0, 0)
        sleep(1)

if __name__ == "__main__":
    main()
