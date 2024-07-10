from search import Problem
from utils import *
import math 

#Function that given two list, choreography, returns the number of common moves between them
def common_el(L1, L2):
    L2 = list(L2)
    #Since these moves are very similar we consider them as the same
    modified_L1 = [item.replace('13-Rotation_foot_LLeg', 'Rotation_foot_Leg')
                         .replace('12-Rotation_foot_RLeg', 'Rotation_foot_Leg')
                         .replace('7-Move_forward', 'Diagonal_')
                         .replace('8-Move_backward', 'Diagonal_')
                         .replace('9-Diagonal_left', 'Diagonal_')
                         .replace('10-Diagonal_right', 'Diagonal_') for item in L1]

    modified_L2 = [item.replace('13-Rotation_foot_LLeg', 'Rotation_foot_Leg')
                         .replace('12-Rotation_foot_RLeg', 'Rotation_foot_Leg')
                         .replace('7-Move_forward', 'Diagonal_')
                         .replace('8-Move_backward', 'Diagonal_')
                         .replace('9-Diagonal_left', 'Diagonal_')
                         .replace('10-Diagonal_right', 'Diagonal_') for item in L2]
    

    set1 = set(modified_L1)
    set2 = set(modified_L2)

    common_elements = set1.intersection(set2)
    if 'Diagonal_' in modified_L2:
       common_elements = len(common_elements)+modified_L2.count('Diagonal_')-1
       return common_elements
    else:
      return len(common_elements)

class NaoProblem(Problem):
  def __init__(self, initial, goal, moves, previous_moves, avg_time, past_chor):
    super().__init__(initial, goal)
    self.available_moves = moves 
    self.previous_moves = previous_moves 
    self.avg_time = avg_time
    self.past_chor = past_chor

  #Function that return true if a move is valid, false otherwise
  def isValid(self, stateT, move_name, move):
    state = dict((key, value) for key, value in stateT)
    #Check if the remaining time is enough
    if state['remaining_time'] < move[0]:
      return False
    #Check if the standing constraint is satisfied
    if 'standing' in move[1]:
      if state['standing'] != move[1]['standing']:
        return False       
    #Check if the move is different from the previous ones
    if len(state['choreography'])>=1 and move_name == state['choreography'][-1]:
       return False
    if len(state['choreography'])>=2 and move_name == state['choreography'][-2]:
       return False
    if len(state['choreography'])>=3 and move_name == state['choreography'][-3]:
       return False
    if len(state['choreography'])>=4 and move_name == state['choreography'][-4]:
       return False
    #Check if the choreography that i'm creating is different from the previous ones, we want to have at most 2 element in common
    if len(self.past_chor)>=1:
      for chor in self.past_chor:
        if common_el(chor, state['choreography'])>=2:
          return False
    return True

  def actions(self, state):
    valid_actions = []
    #We cycle through the moves and return the ones that respect our constraint
    for move_name, move in self.available_moves.items():
        if self.isValid(state, move_name, move):
          valid_actions.append(move_name)
    random.shuffle(valid_actions)
    return valid_actions

  def result(self, stateT, action):
    state = dict((key, value) for key, value in stateT)
    nao_move = self.available_moves[action]

    #We set the postcondition of this action, if the action don't modify the standing state we keep the last one
    if 'standing' in nao_move[2]:
        temp_standing = nao_move[2]['standing']
    else:
        temp_standing = state['standing']

    return (('choreography', (*state['choreography'], action)), ('standing', temp_standing), 
            ('remaining_time', state['remaining_time'] - nao_move[0]), 
            ('moves_done', state['moves_done'] + 1))

  def goal_test(self, stateT):
    state = dict((key, value) for key, value in stateT)
    goal = dict((key, value) for key, value in self.goal)

    #We create an interval to check if we filled the time slot for this step
    goal_remaining_time = goal['remaining_time']
    a = goal_remaining_time
    b = goal_remaining_time + 1

    #Check if we filled the time slot for this step 
    time_constraint = (a <= state['remaining_time'] <= b)
    #Check if the number of the chosen moves respect the goal 
    moves_done_constraint = (state['moves_done'] >= goal['moves_done'])
    #Check if we reached our goal standing state
    standing_constraint = (state['standing'] == goal['standing'])

    return time_constraint and moves_done_constraint and standing_constraint

  #Heuristic function used in A* search
  def h(self, nodeT):
    state = dict((key, value) for key, value in nodeT.state)
    goal = dict((key, value) for key, value in self.goal)
    
    #The cost to reach the goal is calculated by multiplying the number of remaining moves to the average execution time of our moves set
    return (goal['moves_done'] - state['moves_done']) * self.avg_time
