# Choregraphe bezier export in Python.
from naoqi import ALProxy
import sys
def main(robotIP, port):
  names = list()
  times = list()
  keys = list()

  names.append("HeadPitch")
  times.append([0.6, 0.84, 1.04, 1.28, 2.68])
  keys.append([[-0.013848, [3, -0.213333, 0], [3, 0.08, 0]], [0.415673, [3, -0.08, 0], [3, 0.0666667, 0]], [-0.151908, [3, -0.0666667, 0], [3, 0.08, 0]], [0.247837, [3, -0.08, 0], [3, 0.466667, 0]], [0.1733, [3, -0.466667, 0], [3, 0, 0]]])

  names.append("HeadYaw")
  times.append([0.6, 0.84, 1.04, 1.28, 2.68])
  keys.append([[-4.19617e-05, [3, -0.213333, 0], [3, 0.08, 0]], [0.010696, [3, -0.08, -0.00362582], [3, 0.0666667, 0.00302152]], [0.0199001, [3, -0.0666667, 0], [3, 0.08, 0]], [0.010696, [3, -0.08, 0.000972782], [3, 0.466667, -0.00567456]], [-4.19617e-05, [3, -0.466667, 0], [3, 0, 0]]])

  names.append("LAnklePitch")
  times.append([1.44])
  keys.append([[-0.232481, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LAnkleRoll")
  times.append([1.44])
  keys.append([[-0.187148, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LElbowRoll")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[-0.843657, [3, -0.16, 0], [3, 0.133333, 0]], [-1.10137, [3, -0.133333, 0.0449243], [3, 0.24, -0.0808638]], [-1.22102, [3, -0.24, 0], [3, 0.146667, 0]], [-0.74088, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("LElbowYaw")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[-1.3561, [3, -0.16, 0], [3, 0.133333, 0]], [-1.10606, [3, -0.133333, 0], [3, 0.24, 0]], [-1.26559, [3, -0.24, 0], [3, 0.146667, 0]], [-1.25179, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("LHand")
  times.append([0.92, 2.12])
  keys.append([[0.161481, [3, -0.32, 0], [3, 0.4, 0]], [0.161117, [3, -0.4, 0], [3, 0, 0]]])

  names.append("LHipPitch")
  times.append([1.44])
  keys.append([[0.502304, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LHipRoll")
  times.append([1.44])
  keys.append([[0.282256, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LHipYawPitch")
  times.append([1.44])
  keys.append([[-0.343615, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LKneePitch")
  times.append([1.44])
  keys.append([[0.109076, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("LShoulderPitch")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[1.66742, [3, -0.16, 0], [3, 0.133333, 0]], [1.41584, [3, -0.133333, 0], [3, 0.24, 0]], [1.52169, [3, -0.24, -0.0387203], [3, 0.146667, 0.0236624]], [1.60299, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("LShoulderRoll")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[0.214717, [3, -0.16, 0], [3, 0.133333, 0]], [0.15796, [3, -0.133333, 0], [3, 0.24, 0]], [0.16563, [3, -0.24, 0], [3, 0.146667, 0]], [0.16563, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("LWristYaw")
  times.append([0.92, 2.12])
  keys.append([[-0.48632, [3, -0.32, 0], [3, 0.4, 0]], [0.185572, [3, -0.4, 0], [3, 0, 0]]])

  names.append("RAnklePitch")
  times.append([1.44])
  keys.append([[-0.23555, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("RAnkleRoll")
  times.append([1.44])
  keys.append([[-0.0322141, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("RElbowRoll")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[1.1981, [3, -0.16, 0], [3, 0.133333, 0]], [1.36837, [3, -0.133333, -0.0102266], [3, 0.24, 0.0184079]], [1.38678, [3, -0.24, 0], [3, 0.146667, 0]], [1.03089, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("RElbowYaw")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[0.816046, [3, -0.16, 0], [3, 0.133333, 0]], [0.704064, [3, -0.133333, 0], [3, 0.24, 0]], [1.05995, [3, -0.24, -0.00251037], [3, 0.146667, 0.00153411]], [1.06149, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("RHand")
  times.append([0.92, 2.12])
  keys.append([[0.280389, [3, -0.32, 0], [3, 0.4, 0]], [0.280389, [3, -0.4, 0], [3, 0, 0]]])

  names.append("RHipPitch")
  times.append([1.44])
  keys.append([[0.399527, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("RHipRoll")
  times.append([1.44])
  keys.append([[0.0475539, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("RKneePitch")
  times.append([1.44])
  keys.append([[0.254806, [3, -0.493333, 0], [3, 0, 0]]])

  names.append("RShoulderPitch")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[1.37451, [3, -0.16, 0], [3, 0.133333, 0]], [1.07691, [3, -0.133333, 0], [3, 0.24, 0]], [1.23798, [3, -0.24, -0.102831], [3, 0.146667, 0.0628411]], [1.57393, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("RShoulderRoll")
  times.append([0.44, 0.84, 1.56, 2])
  keys.append([[-0.084412, [3, -0.16, 0], [3, 0.133333, 0]], [-0.067538, [3, -0.133333, 0], [3, 0.24, 0]], [-0.081344, [3, -0.24, 0.0138061], [3, 0.146667, -0.00843704]], [-0.16418, [3, -0.146667, 0], [3, 0, 0]]])

  names.append("RWristYaw")
  times.append([0.92, 2.12])
  keys.append([[0.722472, [3, -0.32, 0], [3, 0.4, 0]], [-0.00157596, [3, -0.4, 0], [3, 0, 0]]])

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