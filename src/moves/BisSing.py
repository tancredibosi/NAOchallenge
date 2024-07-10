# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.266667, 1.8, 2])
    keys.append([0.0797261, -0.055266, 0.191709])

    names.append("HeadYaw")
    times.append([0.266667, 1.8, 2])
    keys.append([-0.108956, -0.20253, -0.176453])

    names.append("LAnklePitch")
    times.append([0.266667, 0.666667])
    keys.append([-0.374338, -0.374338])

    names.append("LAnkleRoll")
    times.append([0.266667, 0.666667])
    keys.append([0.016916, 0.016916])

    names.append("LElbowRoll")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([-1.03541, -1.05688, -1.05688, -1.04461, -1.05688, -1.04461, -1.04461])

    names.append("LElbowYaw")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([-1.76261, -1.75341, -1.75495, -1.75034, -1.75495, -1.75034, -1.75034])

    names.append("LHand")
    times.append([0.266667])
    keys.append([0.920024])

    names.append("LHipPitch")
    times.append([0.266667, 0.666667])
    keys.append([-0.162562, -0.162562])

    names.append("LHipRoll")
    times.append([0.266667, 0.666667])
    keys.append([0.101286, 0.101286])

    names.append("LHipYawPitch")
    times.append([0.266667, 0.666667])
    keys.append([-0.395731, -0.395731])

    names.append("LKneePitch")
    times.append([0.266667, 0.666667])
    keys.append([0.789967, 0.789967])

    names.append("LShoulderPitch")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([0.745483, 0.733209, 0.743948, 0.760822, 0.743948, 0.760822, 0.760822])

    names.append("LShoulderRoll")
    times.append([0.266667, 0.933333, 1.33333, 2, 2.33333])
    keys.append([0.515382, 0.516916, 0.501576, 0.501576, 0.50311])

    names.append("LWristYaw")
    times.append([0.266667])
    keys.append([-1.01862])

    names.append("RAnklePitch")
    times.append([0.266667, 0.666667])
    keys.append([-0.207048, -0.207048])

    names.append("RAnkleRoll")
    times.append([0.266667, 0.666667])
    keys.append([0.032256, 0.032256])

    names.append("RElbowRoll")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([1.03242, 0.523136, 1.22264, 0.681137, 1.22264, 0.681137, 1.11066])

    names.append("RElbowYaw")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([0.265341, -0.029188, 0.408002, -0.138102, 0.408002, -0.138102, 0.391128])

    names.append("RHand")
    times.append([0.266667, 0.933333])
    keys.append([0.918933, 0.452752])

    names.append("RHipPitch")
    times.append([0.266667, 0.666667])
    keys.append([-0.032256, -0.032256])

    names.append("RHipRoll")
    times.append([0.266667, 0.666667])
    keys.append([-0.016832, -0.016832])

    names.append("RKneePitch")
    times.append([0.266667, 0.666667])
    keys.append([0.55535, 0.55535])

    names.append("RShoulderPitch")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([0.906636, 0.868286, 0.92351, 0.935783, 0.92351, 0.935783, 0.89283])

    names.append("RShoulderRoll")
    times.append([0.266667, 0.933333, 1.13333, 1.33333, 1.8, 2, 2.33333])
    keys.append([-0.185656, -0.101286, -0.0782759, -0.16418, -0.0782759, -0.16418, -0.075208])

    names.append("RWristYaw")
    times.append([0.266667, 0.933333])
    keys.append([0.961776, 0.682588])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


if __name__ == "__main__":

    robotIP = "127.0.0.1" #"192.168.1.11"

    port = 9559 # Insert NAO port

    if len(sys.argv) == 2:
        robotIP = sys.argv[1]
    elif len(sys.argv) > 2:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)