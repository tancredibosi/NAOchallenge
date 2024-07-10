from naoqi import ALProxy

import sys
import time
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0536481, 0.04291, 0.095066, -0.00617796, -0.0506639])

    names.append("HeadYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.427944, -0.438765, 0.461692, -0.530805, 0.010696])

    names.append("LAnklePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.104485, -0.104485, -0.104485, -0.104485, -0.104485])

    names.append("LAnkleRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0092244, 0.0092244, 0.0092244, 0.0092244, 0.0092244])

    names.append("LElbowRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.509245, -0.509245, -0.509245, -0.492371, -0.366584])

    names.append("LElbowYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.319114, -0.449504, -0.319114, -0.325251, -0.335988])

    names.append("LHand")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.656024, 0.654933, 0.656024, 0.65457, 0.65457])

    names.append("LHipPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0596046, 0.0596046, 0.0596046, 0.0596046, 0.0596046])

    names.append("LHipRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.0324061, -0.0324061, -0.0324061, -0.0324061, -0.0324061])

    names.append("LHipYawPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0183645, 0.0183645, 0.0183645, 0.0183645, 0.0183645])

    names.append("LKneePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0702441, 0.0702441, 0.0702441, 0.0702441, 0.0702441])

    names.append("LShoulderPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([1.37596, 1.44805, 1.37749, 1.39436, 1.47567])

    names.append("LShoulderRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.194775, 0.285283, 0.194775, 0.210117, 0.279146])

    names.append("LWristYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-1.01402, -1.01862, -1.01402, -1.02015, -1.02629])

    names.append("RAnklePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.0951351, -0.0951351, -0.0951351, -0.0951351, -0.0951351])

    names.append("RAnkleRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.00302827, -0.00302827, -0.00302827, -0.00302827, -0.00302827])

    names.append("RElbowRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.526205, 0.48632, 0.526205, 0.506262, 0.423426])

    names.append("RElbowYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.539926, 0.542995, 0.539926, 0.539926, 0.547595])

    names.append("RHand")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.698933, 0.697842, 0.698933, 0.697842, 0.697842])

    names.append("RHipPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0367591, 0.0367591, 0.0367591, 0.0367591, 0.0367591])

    names.append("RHipRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0107584, 0.0107584, 0.0107584, 0.0107584, 0.0107584])

    names.append("RKneePitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.0839559, 0.0839559, 0.0839559, 0.0839559, 0.0839559])

    names.append("RShoulderPitch")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([1.4374, 1.46194, 1.43893, 1.46041, 1.53558])

    names.append("RShoulderRoll")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([-0.242414, -0.308375, -0.242414, -0.262356, -0.346725])

    names.append("RWristYaw")
    times.append([0.266667, 0.6, 0.933333, 1.26667, 1.53333])
    keys.append([0.975581, 0.975581, 0.975581, 0.993989, 0.993989])


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