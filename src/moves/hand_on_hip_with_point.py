# Choregraphe bezier export in Python.
from naoqi import ALProxy
import sys
def main(robotIP, port):
  names = list()
  times = list()
  keys = list()

  names.append("LAnklePitch")
  times.append([0.933333])
  keys.append([[-0.42049, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LAnkleRoll")
  times.append([0.933333])
  keys.append([[-0.0183876, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LElbowRoll")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[-0.42641, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.730143, [3, -0.244444, 0], [3, 0.4, 0]], [-0.730143, [3, -0.4, 0], [3, 0.133333, 0]], [-0.711735, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("LElbowYaw")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[0.285283, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.325251, [3, -0.244444, 0], [3, 0.4, 0]], [-0.325251, [3, -0.4, 0], [3, 0.133333, 0]], [-0.328317, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("LHand")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[0.916387, [3, -0.244444, 0], [3, 0.244444, 0]], [0.916387, [3, -0.244444, 0], [3, 0.4, 0]], [0.916387, [3, -0.4, 0], [3, 0.133333, 0]], [0.916387, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("LHipPitch")
  times.append([0.933333])
  keys.append([[-0.290147, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LHipRoll")
  times.append([0.933333])
  keys.append([[-0.0492801, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LHipYawPitch")
  times.append([0.933333])
  keys.append([[-0.0982195, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LKneePitch")
  times.append([0.933333])
  keys.append([[0.699184, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("LShoulderPitch")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[1.06302, [3, -0.244444, 0], [3, 0.244444, 0]], [0.091998, [3, -0.244444, 0], [3, 0.4, 0]], [0.091998, [3, -0.4, 0], [3, 0.133333, 0]], [0.144154, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("LShoulderRoll")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[0.251533, [3, -0.244444, 0], [3, 0.244444, 0]], [0.279146, [3, -0.244444, 0], [3, 0.4, 0]], [0.279146, [3, -0.4, 0], [3, 0.133333, 0]], [0.297554, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("LWristYaw")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[-0.998676, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.998676, [3, -0.244444, 0], [3, 0.4, 0]], [-0.998676, [3, -0.4, 0], [3, 0.133333, 0]], [-0.998676, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RAnklePitch")
  times.append([0.933333])
  keys.append([[-0.444888, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("RAnkleRoll")
  times.append([0.933333])
  keys.append([[0.0752057, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("RElbowRoll")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[1.56165, [3, -0.244444, 0], [3, 0.244444, 0]], [1.54478, [3, -0.244444, 0], [3, 0.4, 0]], [1.54478, [3, -0.4, 0], [3, 0.133333, 0]], [1.47575, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RElbowYaw")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[-0.188724, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.20253, [3, -0.244444, 0], [3, 0.4, 0]], [-0.20253, [3, -0.4, 0], [3, 0.133333, 0]], [-0.20253, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RHand")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[0.918205, [3, -0.244444, 0], [3, 0.244444, 0]], [0.918205, [3, -0.244444, 0], [3, 0.4, 0]], [0.918205, [3, -0.4, 0], [3, 0.133333, 0]], [0.918205, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RHipPitch")
  times.append([0.933333])
  keys.append([[-0.33907, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("RHipRoll")
  times.append([0.933333])
  keys.append([[-0.0782136, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("RKneePitch")
  times.append([0.933333])
  keys.append([[0.757382, [3, -0.333333, 0], [3, 0, 0]]])

  names.append("RShoulderPitch")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[1.15514, [3, -0.244444, 0], [3, 0.244444, 0]], [1.0631, [3, -0.244444, 0], [3, 0.4, 0]], [1.0631, [3, -0.4, 0], [3, 0.133333, 0]], [1.03396, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RShoulderRoll")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[-1.01555, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.586029, [3, -0.244444, 0], [3, 0.4, 0]], [-0.586029, [3, -0.4, 0], [3, 0.133333, 0]], [-0.828401, [3, -0.133333, 0], [3, 0, 0]]])

  names.append("RWristYaw")
  times.append([0.666667, 1.4, 2.6, 3])
  keys.append([[0.946436, [3, -0.244444, 0], [3, 0.244444, 0]], [0.946436, [3, -0.244444, 0], [3, 0.4, 0]], [0.946436, [3, -0.4, 0], [3, 0.133333, 0]], [0.946436, [3, -0.133333, 0], [3, 0, 0]]])

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