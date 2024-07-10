# Choregraphe bezier export in Python.
from naoqi import ALProxy
import sys
def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0536481, [3, -0.2, 0], [3, 0.2, 0]], [0.04291, [3, -0.2, 0], [3, 0.2, 0]], [0.095066, [3, -0.2, 0], [3, 0.2, 0]], [-0.00617796, [3, -0.2, 0.0242883], [3, 0.2, -0.0242883]], [-0.0506639, [3, -0.2, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.427944, [3, -0.2, 0], [3, 0.2, 0]], [-0.438765, [3, -0.2, 0], [3, 0.2, 0]], [0.461692, [3, -0.2, 0], [3, 0.2, 0]], [-0.530805, [3, -0.2, 0], [3, 0.2, 0]], [0.010696, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.104485, [3, -0.2, 0], [3, 0.2, 0]], [-0.104485, [3, -0.2, 0], [3, 0.2, 0]], [-0.104485, [3, -0.2, 0], [3, 0.2, 0]], [-0.104485, [3, -0.2, 0], [3, 0.2, 0]], [-0.104485, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0092244, [3, -0.2, 0], [3, 0.2, 0]], [0.0092244, [3, -0.2, 0], [3, 0.2, 0]], [0.0092244, [3, -0.2, 0], [3, 0.2, 0]], [0.0092244, [3, -0.2, 0], [3, 0.2, 0]], [0.0092244, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.509245, [3, -0.2, 0], [3, 0.2, 0]], [-0.509245, [3, -0.2, 0], [3, 0.2, 0]], [-0.509245, [3, -0.2, 0], [3, 0.2, 0]], [-0.492371, [3, -0.2, -0.0168739], [3, 0.2, 0.0168739]], [-0.366584, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.319114, [3, -0.2, 0], [3, 0.2, 0]], [-0.449504, [3, -0.2, 0], [3, 0.2, 0]], [-0.319114, [3, -0.2, 0], [3, 0.2, 0]], [-0.325251, [3, -0.2, 0.00281231], [3, 0.2, -0.00281231]], [-0.335988, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.656024, [3, -0.2, 0], [3, 0.2, 0]], [0.654933, [3, -0.2, 0], [3, 0.2, 0]], [0.656024, [3, -0.2, 0], [3, 0.2, 0]], [0.65457, [3, -0.2, 0], [3, 0.2, 0]], [0.65457, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0596046, [3, -0.2, 0], [3, 0.2, 0]], [0.0596046, [3, -0.2, 0], [3, 0.2, 0]], [0.0596046, [3, -0.2, 0], [3, 0.2, 0]], [0.0596046, [3, -0.2, 0], [3, 0.2, 0]], [0.0596046, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.0324061, [3, -0.2, 0], [3, 0.2, 0]], [-0.0324061, [3, -0.2, 0], [3, 0.2, 0]], [-0.0324061, [3, -0.2, 0], [3, 0.2, 0]], [-0.0324061, [3, -0.2, 0], [3, 0.2, 0]], [-0.0324061, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0183645, [3, -0.2, 0], [3, 0.2, 0]], [0.0183645, [3, -0.2, 0], [3, 0.2, 0]], [0.0183645, [3, -0.2, 0], [3, 0.2, 0]], [0.0183645, [3, -0.2, 0], [3, 0.2, 0]], [0.0183645, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0702441, [3, -0.2, 0], [3, 0.2, 0]], [0.0702441, [3, -0.2, 0], [3, 0.2, 0]], [0.0702441, [3, -0.2, 0], [3, 0.2, 0]], [0.0702441, [3, -0.2, 0], [3, 0.2, 0]], [0.0702441, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[1.37596, [3, -0.2, 0], [3, 0.2, 0]], [1.44805, [3, -0.2, 0], [3, 0.2, 0]], [1.37749, [3, -0.2, 0], [3, 0.2, 0]], [1.39436, [3, -0.2, -0.0163625], [3, 0.2, 0.0163625]], [1.47567, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.194775, [3, -0.2, 0], [3, 0.2, 0]], [0.285283, [3, -0.2, 0], [3, 0.2, 0]], [0.194775, [3, -0.2, 0], [3, 0.2, 0]], [0.210117, [3, -0.2, -0.0140618], [3, 0.2, 0.0140618]], [0.279146, [3, -0.2, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-1.01402, [3, -0.2, 0], [3, 0.2, 0]], [-1.01862, [3, -0.2, 0], [3, 0.2, 0]], [-1.01402, [3, -0.2, 0], [3, 0.2, 0]], [-1.02015, [3, -0.2, 0.00204552], [3, 0.2, -0.00204552]], [-1.02629, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.0951351, [3, -0.2, 0], [3, 0.2, 0]], [-0.0951351, [3, -0.2, 0], [3, 0.2, 0]], [-0.0951351, [3, -0.2, 0], [3, 0.2, 0]], [-0.0951351, [3, -0.2, 0], [3, 0.2, 0]], [-0.0951351, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.00302827, [3, -0.2, 0], [3, 0.2, 0]], [-0.00302827, [3, -0.2, 0], [3, 0.2, 0]], [-0.00302827, [3, -0.2, 0], [3, 0.2, 0]], [-0.00302827, [3, -0.2, 0], [3, 0.2, 0]], [-0.00302827, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.526205, [3, -0.2, 0], [3, 0.2, 0]], [0.48632, [3, -0.2, 0], [3, 0.2, 0]], [0.526205, [3, -0.2, 0], [3, 0.2, 0]], [0.506262, [3, -0.2, 0.0171298], [3, 0.2, -0.0171298]], [0.423426, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.539926, [3, -0.2, 0], [3, 0.2, 0]], [0.542995, [3, -0.2, 0], [3, 0.2, 0]], [0.539926, [3, -0.2, 0], [3, 0.2, 0]], [0.539926, [3, -0.2, 0], [3, 0.2, 0]], [0.547595, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.698933, [3, -0.2, 0], [3, 0.2, 0]], [0.697842, [3, -0.2, 0], [3, 0.2, 0]], [0.698933, [3, -0.2, 0], [3, 0.2, 0]], [0.697842, [3, -0.2, 0], [3, 0.2, 0]], [0.697842, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0367591, [3, -0.2, 0], [3, 0.2, 0]], [0.0367591, [3, -0.2, 0], [3, 0.2, 0]], [0.0367591, [3, -0.2, 0], [3, 0.2, 0]], [0.0367591, [3, -0.2, 0], [3, 0.2, 0]], [0.0367591, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0107584, [3, -0.2, 0], [3, 0.2, 0]], [0.0107584, [3, -0.2, 0], [3, 0.2, 0]], [0.0107584, [3, -0.2, 0], [3, 0.2, 0]], [0.0107584, [3, -0.2, 0], [3, 0.2, 0]], [0.0107584, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.0839559, [3, -0.2, 0], [3, 0.2, 0]], [0.0839559, [3, -0.2, 0], [3, 0.2, 0]], [0.0839559, [3, -0.2, 0], [3, 0.2, 0]], [0.0839559, [3, -0.2, 0], [3, 0.2, 0]], [0.0839559, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[1.4374, [3, -0.2, 0], [3, 0.2, 0]], [1.46194, [3, -0.2, 0], [3, 0.2, 0]], [1.43893, [3, -0.2, 0], [3, 0.2, 0]], [1.46041, [3, -0.2, -0.0161071], [3, 0.2, 0.0161071]], [1.53558, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[-0.242414, [3, -0.2, 0], [3, 0.2, 0]], [-0.308375, [3, -0.2, 0], [3, 0.2, 0]], [-0.242414, [3, -0.2, 0], [3, 0.2, 0]], [-0.262356, [3, -0.2, 0.0173852], [3, 0.2, -0.0173852]], [-0.346725, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.533333, 1.13333, 1.73333, 2.33333, 2.93333])
    keys.append([[0.975581, [3, -0.2, 0], [3, 0.2, 0]], [0.975581, [3, -0.2, 0], [3, 0.2, 0]], [0.975581, [3, -0.2, 0], [3, 0.2, 0]], [0.993989, [3, -0.2, 0], [3, 0.2, 0]], [0.993989, [3, -0.2, 0], [3, 0, 0]]])

    try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    # motion = ALProxy("ALMotion", IP, 9559)
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolationBezier(names, times, keys)
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