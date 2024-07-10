# Choregraphe simplified export in Python.

from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("LAnklePitch")
    times.append([0.733333])
    keys.append([-0.42049])

    names.append("LAnkleRoll")
    times.append([0.733333])
    keys.append([-0.0183876])

    names.append("LElbowRoll")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([-0.42641, -0.730143, -0.730143, -0.711735])

    names.append("LElbowYaw")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([0.285283, -0.325251, -0.325251, -0.328317])

    names.append("LHand")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([0.916387, 0.916387, 0.916387, 0.916387])

    names.append("LHipPitch")
    times.append([0.733333])
    keys.append([-0.290147])

    names.append("LHipRoll")
    times.append([0.733333])
    keys.append([-0.0492801])

    names.append("LHipYawPitch")
    times.append([0.733333])
    keys.append([-0.0982195])

    names.append("LKneePitch")
    times.append([0.733333])
    keys.append([0.699184])

    names.append("LShoulderPitch")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([1.06302, 0.091998, 0.091998, 0.144154])

    names.append("LShoulderRoll")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([0.251533, 0.279146, 0.279146, 0.297554])

    names.append("LWristYaw")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([-0.998676, -0.998676, -0.998676, -0.998676])

    names.append("RAnklePitch")
    times.append([0.733333])
    keys.append([-0.444888])

    names.append("RAnkleRoll")
    times.append([0.733333])
    keys.append([0.0752057])

    names.append("RElbowRoll")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([1.56165, 1.54478, 1.54478, 1.47575])

    names.append("RElbowYaw")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([-0.188724, -0.20253, -0.20253, -0.20253])

    names.append("RHand")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([0.918205, 0.918205, 0.918205, 0.918205])

    names.append("RHipPitch")
    times.append([0.733333])
    keys.append([-0.33907])

    names.append("RHipRoll")
    times.append([0.733333])
    keys.append([-0.0782136])

    names.append("RKneePitch")
    times.append([0.733333])
    keys.append([0.757382])

    names.append("RShoulderPitch")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([1.15514, 1.0631, 1.0631, 1.03396])

    names.append("RShoulderRoll")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([-1.01555, -0.586029, -0.586029, -0.828401])

    names.append("RWristYaw")
    times.append([0.4, 1, 1.4, 1.73333])
    keys.append([0.946436, 0.946436, 0.946436, 0.946436])

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