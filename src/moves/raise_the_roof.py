# Choregraphe bezier export in Python.
from naoqi import ALProxy
import sys
def main(robotIP, port):
  names = list()
  times = list()
  keys = list()

  names.append("HeadPitch")
  times.append([3.13333])
  keys.append([[-0.0245859, [3, -1.06667, 0], [3, 0, 0]]])

  names.append("HeadYaw")
  times.append([3.13333])
  keys.append([[0.00609404, [3, -1.06667, 0], [3, 0, 0]]])

  names.append("LAnklePitch")
  times.append([0.8])
  keys.append([[0.10821, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LAnkleRoll")
  times.append([0.8])
  keys.append([[-0.0680678, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LElbowRoll")
  times.append([0.8, 1.06667, 1.33333, 3.13333])
  keys.append([[-1.41124, [3, -0.288889, 0], [3, 0.0888889, 0]], [-1.23395, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-1.41124, [3, -0.0888889, 0], [3, 0.6, 0]], [-0.326699, [3, -0.6, 0], [3, 0, 0]]])

  names.append("LElbowYaw")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[-2.09089, [3, -0.288889, 0], [3, 0.177778, 0]], [-2.09089, [3, -0.177778, 0], [3, 0.6, 0]], [-0.759372, [3, -0.6, 0], [3, 0, 0]]])

  names.append("LHand")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[1, [3, -0.288889, 0], [3, 0.177778, 0]], [1, [3, -0.177778, 0], [3, 0.6, 0]], [0.918933, [3, -0.6, 0], [3, 0, 0]]])

  names.append("LHipPitch")
  times.append([0.8])
  keys.append([[-0.00872665, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LHipRoll")
  times.append([0.8])
  keys.append([[0.0105459, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LHipYawPitch")
  times.append([0.8])
  keys.append([[-0.179521, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LKneePitch")
  times.append([0.8])
  keys.append([[0, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("LShoulderPitch")
  times.append([0.8, 1.06667, 1.33333, 1.6, 1.86667, 2.13333, 2.4, 3.13333])
  keys.append([[0.635035, [3, -0.288889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.635035, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.549779, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.549779, [3, -0.0888889, -0.167277], [3, 0.244444, 0.460011]], [1.56771, [3, -0.244444, 0], [3, 0, 0]]])

  names.append("LShoulderRoll")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[0.37272, [3, -0.288889, 0], [3, 0.177778, 0]], [0.37272, [3, -0.177778, 0], [3, 0.6, 0]], [0.329768, [3, -0.6, 0], [3, 0, 0]]])

  names.append("LWristYaw")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[-1.44862, [3, -0.288889, 0], [3, 0.177778, 0]], [-1.44862, [3, -0.177778, 0], [3, 0.6, 0]], [-1.02629, [3, -0.6, 0], [3, 0, 0]]])

  names.append("RAnklePitch")
  times.append([0.8])
  keys.append([[0.020944, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("RAnkleRoll")
  times.append([0.8])
  keys.append([[0.137881, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("RElbowRoll")
  times.append([0.8, 1.06667, 1.33333, 3.13333])
  keys.append([[1.3607, [3, -0.288889, 0], [3, 0.0888889, 0]], [1.23395, [3, -0.0888889, 0], [3, 0.0888889, 0]], [1.3607, [3, -0.0888889, 0], [3, 0.6, 0]], [0.291501, [3, -0.6, 0], [3, 0, 0]]])

  names.append("RElbowYaw")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[1.9466, [3, -0.288889, 0], [3, 0.177778, 0]], [1.9466, [3, -0.177778, 0], [3, 0.6, 0]], [0.77923, [3, -0.6, 0], [3, 0, 0]]])

  names.append("RHand")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[1, [3, -0.288889, 0], [3, 0.177778, 0]], [1, [3, -0.177778, 0], [3, 0.6, 0]], [0.918205, [3, -0.6, 0], [3, 0, 0]]])

  names.append("RHipPitch")
  times.append([0.8])
  keys.append([[-0.00872665, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("RHipRoll")
  times.append([0.8])
  keys.append([[-0.165652, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("RKneePitch")
  times.append([0.8])
  keys.append([[0, [3, -0.288889, 0], [3, 0, 0]]])

  names.append("RShoulderPitch")
  times.append([0.8, 1.06667, 1.33333, 1.6, 1.86667, 2.13333, 2.4, 3.13333])
  keys.append([[0.676537, [3, -0.288889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.676537, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.549779, [3, -0.0888889, 0], [3, 0.0888889, 0]], [-0.314159, [3, -0.0888889, 0], [3, 0.0888889, 0]], [0.549779, [3, -0.0888889, -0.167284], [3, 0.244444, 0.460032]], [1.56779, [3, -0.244444, 0], [3, 0, 0]]])

  names.append("RShoulderRoll")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[-0.289967, [3, -0.288889, 0], [3, 0.177778, 0]], [-0.289967, [3, -0.177778, 0], [3, 0.6, 0]], [-0.320648, [3, -0.6, 0], [3, 0, 0]]])

  names.append("RWristYaw")
  times.append([0.8, 1.33333, 3.13333])
  keys.append([[1.44862, [3, -0.288889, 0], [3, 0.177778, 0]], [1.44862, [3, -0.177778, 0], [3, 0.6, 0]], [0.967912, [3, -0.6, 0], [3, 0, 0]]])

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