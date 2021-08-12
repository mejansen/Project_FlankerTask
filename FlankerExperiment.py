# import packages:
from expyriment import design, control, stimuli, io, misc
import random

# default settings:
stimuli.defaults.textline_text_size = 50
stimuli.defaults.fixcross_line_width = 3
stimuli.defaults.fixcross_size = (30,30)
control.set_develop_mode(True)
io.defaults.outputfile_time_stamp = False
control.defaults.open_gl = 2



# function to create onset times:
def mean(input_list):
    """Receives a list of integers as input and returns the mean of all entries"""
    return (sum(input_list) / len(input_list))

INSTRUCTIONS = "Press the according key for the middle symbol of the arrow array! Example: <<<<<, >><>> -> left, while >>>>>, <<><< -> right. After pressing any key, the experiment will start automatically after 5 seconds!"
PAUSE_INTRO = "You now have completed the first one of two blocks. You have 5 minutes left, before the second one starts. The counter will refresh every minute."
GOODBYE_TEXT = "Thanks for participating in this experiment, press any key to exit. In order to do something further, restart the menu.py file in a new terminal."

# function to construct the design:
def construct_design(exp, ):
    """This function receives an expyriment object and adds the trials in blocks to it."""
    left_congruent = ["congruent", "left", misc.constants.K_LEFT, "<<<<<"]
    right_congruent = ["congruent", "right", misc.constants.K_RIGHT, ">>>>>"]
    left_incongruent = ["incongruent", "left", misc.constants.K_LEFT, ">><>>"]
    right_incongruent = ["incongruent", "right", misc.constants.K_RIGHT, "<<><<"]

    for counter in [1, 2]:
        block = design.Block("Block")
        block.set_factor("Block", counter)
        for kind in [left_congruent, right_congruent, left_incongruent, right_incongruent]:
            t = design.Trial()
            t.set_factor("Condition", kind[0])
            t.set_factor("Direction", kind[1])
            t.set_factor("Key", kind[2])
            t.set_factor("Block", counter)
            s = stimuli.TextLine(text = kind[3], position = [0, 0])
            t.add_stimulus(s)
            block.add_trial(t, copies = 6)
        block.shuffle_trials()
        exp.add_block(block)

        
def conduct_experiment(exp, blankscreen, fixcross, response_keys):
    """This function conducts the experiment according to the trial order constructe by the previous function."""
    random.seed()

    for block in exp.blocks:
        # generate inter_trial_intervals and set an index:
        inter_trial_intervals = [8, 9, 10, 11, 12, 13, 14]
        onset = random.choices(inter_trial_intervals, k = 23)
        while mean(onset) != 12:
            onset = random.choices(inter_trial_intervals, k = 23)
        onset.insert(0, 0)
        index = 0
        
        # show instructions:
        stimuli.TextScreen("Instructions", INSTRUCTIONS).present()
        exp.keyboard.wait()
        blankscreen.present()
        exp.clock.wait_seconds(5)
        
        # start the trials:
        for trial in block.trials:
            # present fixcross
            exp.clock.wait_seconds(onset[index] - 1)
            fixcross.present(clear = False, update = True)
            exp.clock.wait(900)
            blankscreen.present()
            exp.clock.wait(100 - trial.stimuli[0].preload())
            
            # present stimulus, take button & time and present blankscreen thereafter
            trial.stimuli[0].present()
            button, rt = exp.keyboard.wait(keys = response_keys)
            blankscreen.present() # feedback for the participant that trial was successful

            # transfer the data and update index:
            response_correct = int((button == trial.get_factor("Key")) == True)
            if trial.get_factor("Direction") == "left":
                variance = 1
            else:
                variance = 2
            exp.data.add([response_correct, variance, trial.get_factor("Condition"), sum(onset[:(index + 1)]), rt, block.get_factor("Block")])
            index += 1
            
        # 5-minute-waiting-perios after the first block (with minute counter)
        if block.get_factor("Block") == 1:
            stimuli.TextScreen("Pause", PAUSE_INTRO).present()
            exp.clock.wait_minutes(1)
            
            for minute in [4, 3, 2, 1]:
                stimuli.TextScreen("Pause", "You now have " +str(minute) + " minute(s) left.").present()
                exp.clock.wait_minutes(1)



def main():
    """Main function: calls upon collaborating functions and coordinates the experiment."""
    # Create and initialize an experiment:
    exp = design.Experiment("Flanker Task")
    control.initialize(exp)
    
    # Define and preload standard stimuli:
    fixcross = stimuli.FixCross()
    fixcross.preload()
    blankscreen = stimuli.BlankScreen()
    blankscreen.preload()
    
    # left and right arrow keys for responses:
    response_keys = [misc.constants.K_LEFT, misc.constants.K_RIGHT]
    
    construct_design(exp) # function call -> see function further up
    
    # define variable names for collecting data
    exp.data_variable_names = ["Response", "StimVar", "Condition", "Onset", "RT", "Block"]
    
    # conduct the whole experiment:
    control.start()
    conduct_experiment(exp, blankscreen, fixcross, response_keys)  # function call -> see further up
    stimuli.TextScreen("That's it", GOODBYE_TEXT).present()
    exp.keyboard.wait()
    control.end()


# not yet sure, whether necessary:
if __name__ == "__main__":
    main()