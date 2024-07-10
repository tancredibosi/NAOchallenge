# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.2, 1, 1.26667])
    keys.append([-0.012314, 0.00609404, 0.00609404])

    names.append("HeadYaw")
    times.append([0.2, 1, 1.26667])
    keys.append([0.00762803, 0.00762803, 0.00762803])

    names.append("LAnklePitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.191576, 0.205383, 0.183907, 0.183907])

    names.append("LAnkleRoll")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.0659823, 0.0613804, -0.0107176, -0.0107176])

    names.append("LElbowRoll")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([-1.4772, -1.55697, -0.010696, -0.010696])

    names.append("LElbowYaw")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([-1.71812, -1.29627, -0.216335, -0.216335])

    names.append("LHand")
    times.append([0.2, 1, 1.26667])
    keys.append([0.997114, 0.995296, 0.995296])

    names.append("LHipPitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.179256, 0.162382, -0.24106, -0.24106])

    names.append("LHipRoll")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.0580999, 0.07344, -0.145922, -0.145922])

    names.append("LHipYawPitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([-0.730228, -0.739431, -0.487856, -0.487856])

    names.append("LKneePitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.185295, 0.169954, 0.166886, 0.166886])

    names.append("LShoulderPitch")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([1.53089, 0.179436, 1.7073, 1.7073])

    names.append("LShoulderRoll")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([0.039842, 0, 1.35601, 1.34374])

    names.append("LWristYaw")
    times.append([0.2, 1, 1.26667])
    keys.append([-0.277696, -0.289967, -0.289967])

    names.append("RAnklePitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([-0.411138, -0.401935, 0.352792, 0.352792])

    names.append("RAnkleRoll")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.0322537, 0.0337877, 0.248547, 0.248547])

    names.append("RElbowRoll")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([1.46348, 1.56319, 1.54171, 1.54171])

    names.append("RElbowYaw")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([1.52015, 1.44499, 1.65821, 1.65668])

    names.append("RHand")
    times.append([0.2, 1, 1.26667])
    keys.append([1, 1, 1])

    names.append("RHipPitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.489289, 0.490823, -0.279246, -0.279246])

    names.append("RHipRoll")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([-0.148778, -0.15338, -0.257691, -0.257691])

    names.append("RKneePitch")
    times.append([0.2, 0.466667, 1, 1.26667])
    keys.append([0.47666, 0.455184, 0.0195278, 0.0195278])

    names.append("RShoulderPitch")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([0.00464395, 2.07247, 1.56779, 1.56779])

    names.append("RShoulderRoll")
    times.append([0.2, 0.733333, 1, 1.26667])
    keys.append([-0.11816, -0.154976, -0.182588, -0.182588])

    names.append("RWristYaw")
    times.append([0.2, 1, 1.26667])
    keys.append([0.408002, 0.41107, 0.41107])


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