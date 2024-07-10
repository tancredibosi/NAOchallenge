from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([2.13333])
    keys.append([-0.0245859])

    names.append("HeadYaw")
    times.append([2.13333])
    keys.append([0.00609404])

    names.append("LAnklePitch")
    times.append([0.266667])
    keys.append([0.10821])

    names.append("LAnkleRoll")
    times.append([0.266667])
    keys.append([-0.0680678])

    names.append("LElbowRoll")
    times.append([0.266667, 0.533333, 0.8, 2.13333])
    keys.append([-1.41124, -1.23395, -1.41124, -0.326699])

    names.append("LElbowYaw")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([-2.09089, -2.09089, -0.759372])

    names.append("LHand")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([1, 1, 0.918933])

    names.append("LHipPitch")
    times.append([0.266667])
    keys.append([-0.00872665])

    names.append("LHipRoll")
    times.append([0.266667])
    keys.append([0.0105459])

    names.append("LHipYawPitch")
    times.append([0.266667])
    keys.append([-0.179521])

    names.append("LKneePitch")
    times.append([0.266667])
    keys.append([0])

    names.append("LShoulderPitch")
    times.append([0.266667, 0.533333, 0.8, 1.06667, 1.33333, 1.6, 1.86667, 2.13333])
    keys.append([0.635035, -0.314159, 0.635035, -0.314159, 0.549779, -0.314159, 0.549779, 1.56771])

    names.append("LShoulderRoll")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([0.37272, 0.37272, 0.329768])

    names.append("LWristYaw")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([-1.44862, -1.44862, -1.02629])

    names.append("RAnklePitch")
    times.append([0.266667])
    keys.append([0.020944])

    names.append("RAnkleRoll")
    times.append([0.266667])
    keys.append([0.137881])

    names.append("RElbowRoll")
    times.append([0.266667, 0.533333, 0.8, 2.13333])
    keys.append([1.3607, 1.23395, 1.3607, 0.291501])

    names.append("RElbowYaw")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([1.9466, 1.9466, 0.77923])

    names.append("RHand")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([1, 1, 0.918205])

    names.append("RHipPitch")
    times.append([0.266667])
    keys.append([-0.00872665])

    names.append("RHipRoll")
    times.append([0.266667])
    keys.append([-0.165652])

    names.append("RKneePitch")
    times.append([0.266667])
    keys.append([0])

    names.append("RShoulderPitch")
    times.append([0.266667, 0.533333, 0.8, 1.06667, 1.33333, 1.6, 1.86667, 2.13333])
    keys.append([0.676537, -0.314159, 0.676537, -0.314159, 0.549779, -0.314159, 0.549779, 1.56779])

    names.append("RShoulderRoll")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([-0.289967, -0.289967, -0.320648])

    names.append("RWristYaw")
    times.append([0.266667, 0.8, 2.13333])
    keys.append([1.44862, 1.44862, 0.967912])

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