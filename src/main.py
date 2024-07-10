from Nao import NaoProblem
from utils import *
from search import *

import vlc
import subprocess
import time
import math

#Function that uses vlc library to play a song given in input 
def play_song(song_name):
    p = vlc.MediaPlayer(song_name)
    try:
        c = p.play()
        time.sleep(2)
    except Exception as e:
        print(e)

#Function that actually makes the robot moves
def do_moves(moves, ip, port):
    for move in moves:
        print(f"\n {move} ", end="", flush=True)
        command = f"python2 ./moves/{move}.py  {ip} {port}"
        start_move = time.time()
        process = subprocess.run(command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        # We used this print in testing to adjust the execution time of our moves set
        #print("\nExecution time: %.2f seconds." % (end_move-start_move), flush=True)

def main(ip, port):

    #Dictionary of moves available with the execution time, precondition and postcondition
    moves = {'2-Right_arm': [13.498584270477295, {}, {}], 
             '3-Double_movement': [7.9943461418151855, {}, {}], 
             '4-Arms_opening': [7.53334903717041, {}, {}], 
             '5-Union_arms': [10.869457244873047, {}, {}], 
             '7-Move_forward': [7.066644906997681, {}, {'standing': True}], 
             '8-Move_backward': [5.388515949249268, {}, {'standing': True}],
             '9-Diagonal_left': [3.675786256790161, {}, {'standing': True}], 
             '10-Diagonal_right': [3.85556697845459, {}, {'standing': True}], 
             #'12-Rotation_foot_RLeg': [8.006103515625, {'standing': True}, {'standing': True}], 
             #'13-Rotation_foot_LLeg': [8.65566611289978, {'standing': True}, {'standing': True}], 
             'AirGuitar': [6.247925281524658, {}, {}], 
             'birthday_dance_no_sound': [13.914993047714233, {}, {}], 
             'BlowKisses': [6.448557376861572, {'standing': True}, {'standing': True}], 
             'Bow': [5.640871047973633, {'standing': True}, {'standing': True}], 
             'ComeOn': [5.608509540557861, {'standing': True}, {'standing': True}], 
             'Dab': [4.805154800415039, {}, {}], 
             'DanceMove': [8.894711017608643, {'standing': True}, {'standing': True}], 
             'Disco': [22.164984226226807, {}, {}], 
             'do_clapping_nosound': [6.495915412902832, {}, {}], 
             'Glory': [5.377662897109985, {}, {}], 
             'hand_on_hip_with_point': [4.854234457015991, {}, {}], 
             'hands_on_hips': [3.411938190460205, {}, {}], 
             #'head_nod': [4.4284749031066895, {}, {}], 
             'Headbang': [17.47127628326416, {}, {}], 
             'raise_the_roof': [5.058943510055542, {}, {}], 
             'Rhythm': [4.874321222305298, {'standing': True}, {'standing': True}], 
             'shake_head': [5.285283327102661, {}, {}], 
             'sing_with_me': [20.584619522094727, {}, {}], 
             'sprinkler_left': [12.87248969078064, {'standing': True}, {'standing': True}], 
             'sprinkler_right': [11.470921754837036, {'standing': True}, {'standing': True}], 
             'StayingAlive': [8.643508672714233, {'standing': True}, {'standing': True}], 
             'the_robot_2': [6.340930938720703, {'standing': True}, {'standing': True}], 
             'Wave': [5.631593942642212, {}, {}],
             '16-Sit': [3.8506929874420166, {'standing': True}, {'standing': False}], 
             'BisDisco':  [3.295485496520996, {'standing': True}, {'standing': True}],
             'BisHandsPoint': [2.9496712684631348, {'standing': True}, {'standing': True}], 
             'BisHeadNod': [2.755136489868164, {'standing': True}, {'standing': True}],
             'BisRaiseRoof': [3.2126669883728027, {'standing': True}, {'standing': True}], 
             'BisRobot': [2.026519775390625, {'standing': True}, {'standing': True}], 
             'BisShakeHead': [2.3920693397521973, {'standing': True}, {'standing': True}], 
             'BisSing': [3.432499885559082, {'standing': True}, {'standing': True}],
             'BisClap': [2.4191088676452637, {'standing': True}, {'standing': True}], 
             'BisBirthdayA': [2.778902769088745, {'standing': True}, {'standing': True}], 
             'BisBirthdayB': [3.007429838180542, {'standing': True}, {'standing': True}],
             'BisHeadNod': [2.556999683380127, {'standing': True}, {'standing': True}]}

    #Dictionary of mandatory moves with the execution time, precondition and postcondition
    Mmoves = {'6-Crouch': [2.8168132305145264, {'standing': True}, {'standing': True}], 
             'M_WipeForehead': [6.363635301589966, {'standing': True}, {'standing': True}], 
             'Hello': [6.2890472412109375, {'standing': True}, {'standing': True}], 
             '11-Stand': [1.5150482654571533, {'standing': True}, {'standing': True}], 
             '14-StandInit': [1.1120691299438477, {'standing': True}, {'standing': True}], 
             '15-StandZero': [1.613008737564087, {'standing': True}, {'standing': True}], 
             '16-Sit': [3.8506929874420166, {'standing': True}, {'standing': False}], 
             '17-SitRelax': [2.084895133972168, {'standing': False}, {'standing': False}], 
            }

    start_pos = '14-StandInit'
    mandatory_pos = ['11-Stand', '15-StandZero', 'Hello', 'M_WipeForehead', '16-Sit', '17-SitRelax']
    end_pos = '6-Crouch'
    pos_list = [start_pos, *mandatory_pos, end_pos]

    #We calculate the time used by the mandatory moves
    time_used = 0.0
    for pos in pos_list:
        time_used += Mmoves[pos][0]
        
    #We calculate the average duration of the available moves
    avg_time = 0.0
    for pos in moves.values():
        avg_time += pos[0]
    avg_time = avg_time/len(moves)
    print(f"Average execution time: {avg_time}")
    
    solution = []
    print("SOLUTION:")
    starting_time = time.time()
    interval_time = (180 - time_used) / (len(pos_list) - 1)
    print(f"Interval time: {interval_time} \nTime used for mandatory moves: {time_used}")
    
    waste = 0.0
    past_chor = []

    #We iterate through the mandatory position in order to create a choreograpy for each interval
    for i in range(1, len(pos_list)):

        initial_pos = pos_list[i - 1]
        final_pos = pos_list[i]
        initial_standing = Mmoves[initial_pos][1]['standing']
        final_standing = Mmoves[final_pos][1]['standing']
        choreography = (initial_pos, ) 

        cur_state = (
            ('choreography', choreography),
            ('standing', initial_standing),
            ('remaining_time', interval_time + waste),
            ('moves_done', 0))
        
        cur_goal_state = (
            ('standing', final_standing),
            ('remaining_time', 0),
            ('moves_done', 5))
        
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, tuple(solution), avg_time, past_chor)
        cur_solutionTuple = astar_search(cur_problem)
        
        if cur_solutionTuple is None:
            raise RuntimeError(f'In step {i} i could not find a solution!')
        
        cur_solution = dict((key, value) for key, value in cur_solutionTuple.state)

        #We take track of each choreography in order to make comparison between them and avoid repetitions
        past_chor.append(list(cur_solution['choreography']))

        print('Step ', i, ':')
        for j in cur_solution['choreography']:
            print(' ' + j)
        
        #We save the remaining time
        waste = cur_solution['remaining_time']
        for e in [*cur_solution['choreography']]:
            solution.append(e)
        
    ending_time = time.time()
    solution.append(end_pos)
    
    #Execution of the entire choreography
    print('\n--------Executing dance--------')
    
    play_song("music.mp3") 
    start_dance = time.time()
    do_moves(solution, ip, port)
    end_dance = time.time()
    
    print('\nRESULTS:')
    print('Planning time: %.2f s.' % (ending_time - starting_time))
    print('Estimated duration: %.2f s.' % (180 - waste))
    print('Real duration: %.2f s.' % (end_dance - start_dance))



if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559  # Standard NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]

    main(robot_ip, port)