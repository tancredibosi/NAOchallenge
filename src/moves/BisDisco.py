# Choregraphe simplified export in Python.
from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.136568, 0.118076, -0.268493, -0.144238])

    names.append("HeadYaw")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.021518, -0.214803, 0.384992, -0.032256])

    names.append("LAnklePitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.095066, 0.179436, 0.174835, 0.093532])

    names.append("LAnkleRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.116542, -0.141086, -0.0720561, -0.116542])

    names.append("LElbowRoll")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([-0.38806, -1.22562, -0.391128, -1.22562, -0.199378, -0.427944])

    names.append("LElbowYaw")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([-1.20883, -0.803859, -0.337522, -0.803859, -1.56165, -1.17509])

    names.append("LHand")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([0.3056, 0.8592, 0.8592, 0.8592, 0.8592, 0.3048])

    names.append("LHipPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.136568, 0.0552659, -0.243864, 0.138102])

    names.append("LHipRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.116626, 0.142704, 0.066004, 0.11816])

    names.append("LHipYawPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.1733, -0.538392, -0.371186, -0.171766])

    names.append("LKneePitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.090548, -0.00310993, 0.223922, -0.090548])

    names.append("LShoulderPitch")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([1.53089, 0.759288, 0.960242, 0.759288, -1.08611, 1.48027])

    names.append("LShoulderRoll")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([0.130348, 0.228525, -0.314159, 0.228525, 0.636569, 0.0873961])

    names.append("LWristYaw")
    times.append([0.2, 0.6, 0.92, 1.24, 1.56, 1.88])
    keys.append([0.0843279, 1.23176, 0.730143, 1.23176, 0.900415, 0.145688])

    names.append("RAnklePitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.101286, 0.108956, 0.11049, 0.107422])

    names.append("RAnkleRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.075208, -0.0168321, 0.277696, 0.07214])

    names.append("RElbowRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.389678, 0.194861, 0.392746, 0.389678])

    names.append("RElbowYaw")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([1.1796, 1.16887, 1.18114, 1.17654])

    names.append("RHand")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.3068, 0.684, 0.3068, 0.3068])

    names.append("RHipPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.130348, -0.073674, 0.131882, 0.131882])

    names.append("RHipRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.06592, 0.00771189, -0.292952, -0.06592])

    names.append("RHipYawPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.1733, -0.538392, -0.371186, -0.171766])

    names.append("RKneePitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.0923279, 0.196393, -0.0923279, -0.091998])

    names.append("RShoulderPitch")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([1.52637, 1.49262, 1.51563, 1.49569])

    names.append("RShoulderRoll")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([-0.10282, -0.158044, -0.10282, -0.104354])

    names.append("RWristYaw")
    times.append([0.2, 0.92, 1.56, 1.88])
    keys.append([0.059784, -0.530805, 0.06592, 0.0720561])




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