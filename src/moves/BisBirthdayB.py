# Choregraphe simplified export in Python.

from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.1335, -0.145772, -0.1335, -0.145772, -0.1335])

    names.append("HeadYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-4.19617e-05, -4.19617e-05, -4.19617e-05, -4.19617e-05, -4.19617e-05])

    names.append("LAnklePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.0139794, -0.0262515, -0.0139794, -0.0262515, 0.00749657])

    names.append("LAnkleRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.259225, -0.254624, -0.259225, -0.254624, 0.0092244])

    names.append("LElbowRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.814512, -0.653443, -0.814512, -0.653443, -0.558334])

    names.append("LElbowYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-1.66903, -1.42666, -1.66903, -1.42666, -1.86232])

    names.append("LHand")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.421116, 0.421116, 0.421116, 0.421116, 1])

    names.append("LHipPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.286637, 0.303511, 0.286637, 0.303511, 0.378677])

    names.append("LHipRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.22684, 0.211501, 0.22684, 0.211501, -0.0324061])

    names.append("LHipYawPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.346727, -0.337524, -0.346727, -0.337524, -0.369738])

    names.append("LKneePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.0226902, 0.0380302, 0.0226902, 0.0380302, 0.0119521])

    names.append("LShoulderPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.72409, 1.62907, -0.72409, 1.62907, 0.708667])

    names.append("LShoulderRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.314428, 0.059784, 0.314428, 0.059784, 0])

    names.append("LWristYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.690342, -0.681137, -0.690342, -0.681137, -0.690342])

    names.append("RAnklePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.458693, -0.466362, -0.458693, -0.466362, -0.167233])

    names.append("RAnkleRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.00310773, 0.00157374, 0.00310773, 0.00157374, 0.147304])

    names.append("RElbowRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([1.33616, 1.25485, 1.33616, 1.25485, 0.553816])

    names.append("RElbowYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([1.26397, 1.27931, 1.26397, 1.27931, 1.7886])

    names.append("RHand")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.414571, 0.414571, 0.414571, 0.414571, 1])

    names.append("RHipPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.047497, 0.0520989, 0.047497, 0.0520989, 0.243849])

    names.append("RHipRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.0598056, -0.0552035, -0.0598056, -0.0552035, -0.200933])

    names.append("RKneePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.686818, 0.708295, 0.686818, 0.708295, 0.243493])

    names.append("RShoulderPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.615176, -0.530721, 0.615176, -0.530721, 0.529271])

    names.append("RShoulderRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([-0.460242, -0.679603, -0.460242, -0.679603, -0.00924597])

    names.append("RWristYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.6])
    keys.append([0.77923, 0.777696, 0.77923, 0.777696, 0.77923])


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