from naoqi import ALProxy

import sys
import time
def main(robotIP, port):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.133333, 1.2])
    keys.append([-0.00771196, -0.00771196])

    names.append("HeadYaw")
    times.append([0.133333, 1.2])
    keys.append([-0.00157596, -0.00157596])

    names.append("LAnklePitch")
    times.append([0.133333, 1.2])
    keys.append([-0.0922134, -0.0922134])

    names.append("LAnkleRoll")
    times.append([0.133333, 1.2])
    keys.append([0.0046224, 0.0046224])

    names.append("LElbowRoll")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([-0.312894, -1.20253, -1.20253, -1.20253, -0.312894])

    names.append("LElbowYaw")
    times.append([0.133333, 0.333333, 0.466667, 0.6, 0.733333, 0.866667, 1, 1.2])
    keys.append([-0.770111, -0.541052, -0.907571, -0.541052, -0.907571, -0.541052, -0.907571, -0.770111])

    names.append("LHand")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([0.916751, 0.945455, 0.945455, 0.945455, 0.916751])

    names.append("LHipPitch")
    times.append([0.133333, 1.2])
    keys.append([0.0442645, 0.0442645])

    names.append("LHipRoll")
    times.append([0.133333, 1.2])
    keys.append([-0.0155321, -0.0155321])

    names.append("LHipYawPitch")
    times.append([0.133333, 1.2])
    keys.append([0.00916048, 0.00916048])

    names.append("LKneePitch")
    times.append([0.133333, 1.2])
    keys.append([0.0564382, 0.0564382])

    names.append("LShoulderPitch")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([1.57231, 0.994838, 0.994838, 0.994838, 1.57231])

    names.append("LShoulderRoll")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([0.31903, 0, 0, 0, 0.31903])

    names.append("LWristYaw")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([-1.00941, 0.254818, 0.254818, 0.254818, -1.00941])

    names.append("RAnklePitch")
    times.append([0.133333, 1.2])
    keys.append([-0.0889992, -0.0889992])

    names.append("RAnkleRoll")
    times.append([0.133333, 1.2])
    keys.append([-0.00149427, -0.00149427])

    names.append("RElbowRoll")
    times.append([0.133333, 0.333333, 0.466667, 0.6, 0.733333, 0.866667, 1, 1.2])
    keys.append([0.308375, 1.09956, 0.787143, 1.09956, 0.787143, 1.09956, 0.787143, 0.308375])

    names.append("RElbowYaw")
    times.append([0.133333, 0.333333, 0.466667, 0.6, 0.733333, 0.866667, 1, 1.2])
    keys.append([0.770025, 0.541052, 0.518363, 0.541052, 0.518363, 0.541052, 0.518363, 0.770025])

    names.append("RHand")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([0.917114, 0.945455, 0.945455, 0.945455, 0.917114])

    names.append("RHipPitch")
    times.append([0.133333, 1.2])
    keys.append([0.032157, 0.032157])

    names.append("RHipRoll")
    times.append([0.133333, 1.2])
    keys.append([0.0046224, 0.0046224])

    names.append("RKneePitch")
    times.append([0.133333, 1.2])
    keys.append([0.0624798, 0.0624798])

    names.append("RShoulderPitch")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([1.57239, 1.09956, 1.09956, 1.09956, 1.57239])

    names.append("RShoulderRoll")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([-0.309909, -0.0942478, -0.0942478, -0.0942478, -0.309909])

    names.append("RWristYaw")
    times.append([0.133333, 0.333333, 0.6, 0.866667, 1.2])
    keys.append([0.989389, 1.22173, 1.22173, 1.22173, 0.989389])



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