
def Survival(current_life, past_life, reproductions):
    """
    Creates a reward signal 

    current_life : type int

    past_life : type list

    repreoductions: type list
    """

    # NOTE: 
    # life     - amount of energy an agent has at a given time
    # energy   - currency of survival, spent on actions
    # reward   - energy transacted from actions (+/-)
    # fitness  - probability of an individual reproducing
    # survival - probability of an individual receiving energy
    #
    # fitness is relative to the environment...
    # therefore, the reward is relative to the environment
    # so... how do we determine survival?

    reward = 0
    
    # attempt I - distance from previous life score
    reward = current_life - past_life[-1] 
    
    # attempt II - distance from best life value
    reward = current_life - max(past_life)

    # attempt III - time alive or total number of life scores
    reward = len(past_life) + 1

    # attempt IV - number of reproductions
    reward = len(reproductions)

    # cleanup - add current to past
    past_life.append(current_life)    

    return reward

