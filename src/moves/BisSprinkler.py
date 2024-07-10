# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.12, 0.48, 1.36])
    keys.append([-0.12583, -0.233874, -0.173384])

    names.append("HeadYaw")
    times.append([0.12, 0.48, 1.36])
    keys.append([-0.0107799, 0.912807, 0.21932])

    names.append("LAnklePitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.095066, -0.214803, -0.406552])

    names.append("LAnkleRoll")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.116542, -0.14262, -0.11961])

    names.append("LElbowRoll")
    times.append([0.12, 0.4, 0.68, 1.36])
    keys.append([-0.400331, -0.0349066, -0.0459781, -0.358915])

    names.append("LElbowYaw")
    times.append([0.12, 0.4, 0.68, 1.36])
    keys.append([-1.21037, -1.48956, -1.48035, -1.26099])

    names.append("LHand")
    times.append([0.12, 0.4, 0.68, 1.36])
    keys.append([0.3056, 0.9616, 0.9592, 0.9616])

    names.append("LHipPitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.136568, -0.144154, -0.268407])

    names.append("LHipRoll")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.115092, 0.233211, 0.173384])

    names.append("LHipYawPitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.1733, -0.288349, -0.28068])

    names.append("LKneePitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.090548, 0.539926, 0.820649])

    names.append("LShoulderPitch")
    times.append([0.12, 0.4, 0.48, 0.68, 1.36])
    keys.append([1.53089, -0.420357, -0.560251, -0.417134, -0.0966839])

    names.append("LShoulderRoll")
    times.append([0.12, 0.4, 0.68, 0.92, 1.04, 1.36])
    keys.append([0.13495, 0.819114, 0.461692, 0.610865, 0.223402, -0.159578])

    names.append("LWristYaw")
    times.append([0.12, 0.4, 0.68, 0.92, 1.04, 1.36])
    keys.append([0.121144, 0.312894, 0.131882, 0.0663225, 0.0663225, -0.29457])

    names.append("RAnklePitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.10282, -0.0199001, -0.263807])

    names.append("RAnkleRoll")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.07214, 0.116626, 0.0828778])

    names.append("RElbowRoll")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([0.385075, 1.54462, 1.53864, 1.54462, 1.53864, 1.53864, 1.53558])

    names.append("RElbowYaw")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([1.18421, 0.966378, 1.38823, 0.966378, 1.38823, 1.38823, 1.36982])

    names.append("RHand")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([0.3068, 0.7708, 0.7696, 0.7708, 0.7696, 0.7696, 0.7692])

    names.append("RHipPitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([0.130348, 0.138018, -0.251617])

    names.append("RHipRoll")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.06592, -0.0383082, -0.0291041])

    names.append("RHipYawPitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.1733, -0.288349, -0.28068])

    names.append("RKneePitch")
    times.append([0.12, 0.24, 1.36])
    keys.append([-0.0904641, 0.0798099, 0.676537])

    names.append("RShoulderPitch")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([1.51103, -0.742414, -0.566003, -0.742414, -0.566003, -0.566003, -0.544529])

    names.append("RShoulderRoll")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([-0.113558, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.0614019, -0.075208])

    names.append("RWristYaw")
    times.append([0.12, 0.44, 0.64, 0.88, 1.04, 1.2, 1.36])
    keys.append([0.105804, 1.30539, 0.803775, 1.30539, 0.803775, 0.803775, 0.820649])

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