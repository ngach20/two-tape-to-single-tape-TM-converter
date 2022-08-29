from asyncio import shield
from machine import Machine

#General idea:
# --- [FIRST TAPE] # [SECOND TAPE] ---

#For characters that are inside the tape heads:
#0 is replaced by O
#1 is replaced by I
#_ is replaced by E

HASH_TAG = "3"
DOLLAR_SIGN = "4"
AMPERSAND_SIGN = "5"

dot_version_of = {"0" : "O", "1" : "I", "_" : "E"}

shifting_machine_added_to = {}

m = Machine()

#Assuming the tape head is pointing at a hash_tag
#shift it one to the right and return to the original position
def shift_ampersand_machine(parent_state : int):
    shift_state = m.add_state()

    m.add_transition(parent_state, shift_state, AMPERSAND_SIGN, "_", "R")
    m.add_transition(shift_state, parent_state, "_", AMPERSAND_SIGN, "L")


#def add_second_shifting_machine(parent_state : int):
#
#    start_state = m.add_state()
#
#    q0_state = m.add_state()
#    q1_state = m.add_state()
#    q__state = m.add_state()
#    qI_state = m.add_state()
#    qE_state = m.add_state()
#    qO_state = m.add_state()
#    qAmper_state = m.add_state()
#
#    m.add_transition(parent_state, start_state, HASH_TAG, "_", "R")
#
#    m.add_transition(parent_state, q0_state, "0", HASH_TAG, "R")
#    m.add_transition(parent_state, q1_state, "1", HASH_TAG, "R")
#    m.add_transition(parent_state, q__state, "_", HASH_TAG, "R")
#    m.add_transition(parent_state, qI_state, "I", HASH_TAG, "R")
#    m.add_transition(parent_state, qE_state, "E", HASH_TAG, "R")
#    m.add_transition(parent_state, qO_state, "O", HASH_TAG, "R")
#    m.add_transition(parent_state, qAmper_state, AMPERSAND_SIGN, HASH_TAG, "R")
#
#    m.add_transition(q0_state, q0_state, "0", "0", "R")
#    m.add_transition(q1_state, q1_state, "1", "1", "R")
#    m.add_transition(q__state, q__state, "_", "_", "R")
#    m.add_transition(qI_state, qI_state, dot_version_of["1"], dot_version_of["1"], "R")
#    m.add_transition(qE_state, qE_state, dot_version_of["_"], dot_version_of["_"], "R")
#    m.add_transition(qO_state, qO_state, dot_version_of["0"], dot_version_of["0"], "R")
#
#    #--------------------------0#
#    m.add_transition(q0_state, q1_state, "1", "0", "R")
#    m.add_transition(q0_state, q__state, "_", "0", "R")
#    m.add_transition(q0_state, qE_state, dot_version_of["_"], "0", "R")
#    m.add_transition(q0_state, qI_state, dot_version_of["1"], "0", "R")
#    m.add_transition(q0_state, qO_state, dot_version_of["0"], "0", "R")
#    m.add_transition(q0_state, qAmper_state, AMPERSAND_SIGN, "0", "R")
#
#    #--------------------------1#
#    m.add_transition(q1_state, q0_state, "0", "1", "R")
#    m.add_transition(q1_state, q__state, "_", "1", "R")
#    m.add_transition(q1_state, qE_state, dot_version_of["_"], "1", "R")
#    m.add_transition(q1_state, qI_state, dot_version_of["1"], "1", "R")
#    m.add_transition(q1_state, qO_state, dot_version_of["0"], "1", "R")
#    m.add_transition(q1_state, qAmper_state, AMPERSAND_SIGN, "1", "R")
#
#    #--------------------------_#
#    m.add_transition(q__state, q1_state, "1", "_", "R")
#    m.add_transition(q__state, q0_state, "0", "_", "R")
#    m.add_transition(q__state, qE_state, dot_version_of["_"], "_", "R")
#    m.add_transition(q__state, qI_state, dot_version_of["1"], "_", "R")
#    m.add_transition(q__state, qO_state, dot_version_of["0"], "_", "R")
#    m.add_transition(q__state, qAmper_state, AMPERSAND_SIGN, "_", "R")
#
#    #--------------------------E#
#    m.add_transition(qE_state, q1_state, "1", dot_version_of["_"], "R")
#    m.add_transition(qE_state, q__state, "_", dot_version_of["_"], "R")
#    m.add_transition(qE_state, q0_state, "0", dot_version_of["_"], "R")
#    m.add_transition(qE_state, qI_state, dot_version_of["1"], dot_version_of["_"], "R")
#    m.add_transition(qE_state, qO_state, dot_version_of["0"], dot_version_of["_"], "R")
#    m.add_transition(qE_state, qAmper_state, AMPERSAND_SIGN, dot_version_of["_"], "R")
#
#    #--------------------------I#
#    m.add_transition(qI_state, q1_state, "1", dot_version_of["1"], "R")
#    m.add_transition(qI_state, q__state, "_", dot_version_of["1"], "R")
#    m.add_transition(qI_state, qE_state, dot_version_of["_"], dot_version_of["1"], "R")
#    m.add_transition(qI_state, q0_state, "0", dot_version_of["1"], "R")
#    m.add_transition(qI_state, qO_state, dot_version_of["0"], dot_version_of["1"], "R")
#    m.add_transition(qI_state, qAmper_state, AMPERSAND_SIGN, dot_version_of["1"], "R")
#
#    #--------------------------O#
#    m.add_transition(qO_state, q1_state, "1", dot_version_of["0"], "R")
#    m.add_transition(qO_state, q__state, "_", dot_version_of["0"], "R")
#    m.add_transition(qO_state, qE_state, dot_version_of["_"], dot_version_of["0"], "R")
#    m.add_transition(qO_state, q0_state, "0", dot_version_of["0"], "R")
#    m.add_transition(qO_state, qI_state, dot_version_of["1"], dot_version_of["0"], "R")
#    m.add_transition(qO_state, qAmper_state, AMPERSAND_SIGN, dot_version_of["0"], "R")
#
#    return qAmper_state

def add_second_shifting_machine(parent_state):
    loop_state = m.add_state()

    m.add_transition(parent_state, loop_state, HASH_TAG, HASH_TAG, "R")

    for ch in ["0", "1", "_", dot_version_of["0"], dot_version_of["1"], dot_version_of["_"]]:
        m.add_transition(loop_state, loop_state, ch, ch, "R")

    found_end_state = m.add_state()

    m.add_transition(loop_state, found_end_state, AMPERSAND_SIGN, "_", "R")

    empty_char_state = m.add_state()

    m.add_transition(found_end_state, empty_char_state, "_", AMPERSAND_SIGN, "L")

    read_next_state = m.add_state()


    m.add_transition(empty_char_state, read_next_state, "_", "_", "L")

    q0_state = m.add_state()
    q1_state = m.add_state()
    q__state = m.add_state()
    qI_state = m.add_state()
    qE_state = m.add_state()
    qO_state = m.add_state()

    m.add_transition(read_next_state, q0_state, "0", "_", "R")
    m.add_transition(read_next_state, q1_state, "1", "_", "R")
    m.add_transition(read_next_state, q__state, "_", "_", "R")
    m.add_transition(read_next_state, qI_state, dot_version_of["1"], "_", "R")
    m.add_transition(read_next_state, qE_state, dot_version_of["_"], "_", "R")
    m.add_transition(read_next_state, qO_state, dot_version_of["0"], "_", "R")

    m.add_transition(q0_state, empty_char_state, "_", "0", "L")
    m.add_transition(q1_state, empty_char_state, "_", "1", "L")
    m.add_transition(q__state, empty_char_state, "_", "_", "L")
    m.add_transition(qI_state, empty_char_state, "_", dot_version_of["1"], "L")
    m.add_transition(qE_state, empty_char_state, "_", dot_version_of["_"], "L")
    m.add_transition(qO_state, empty_char_state, "_", dot_version_of["0"], "L")

    qHashTag_state = m.add_state()
    m.add_transition(read_next_state, qHashTag_state, HASH_TAG, "_", "R")
    
    return qHashTag_state



    
    


#Shift the string one to the right
#leaving an empty character at the begging
#leaves the tape head at the end of the string
#Adds 4 new states to the machine
def add_shifting_machine():
    start_state = m.add_state()

    q0_state = m.add_state()
    q1_state = m.add_state()

    accept_state = m.add_state()

    m.add_transition(start_state, q0_state, "0", "_", "R")
    m.add_transition(start_state, q1_state, "1", "_", "R")

    m.add_transition(q0_state, q0_state, "0", "0", "R")
    m.add_transition(q1_state, q1_state, "1", "1", "R")

    m.add_transition(q0_state, q1_state, "1", "0", "R")
    m.add_transition(q1_state, q0_state, "0", "1", "R")

    m.add_transition(start_state, accept_state, "_", "_", "R")
    m.add_transition(q0_state, accept_state, "_", "0", "R")
    m.add_transition(q1_state, accept_state, "_", "1", "R")

    return accept_state

#Add boundary indicators to the beginning and end
#(Assuming we are at the end of the string)
# ($SOME_STRING#I#)
#Adds 4 new states to the machine
def add_boundary_machine(parent_state : int):
    put_first_hashtag_at_end_state = parent_state
    go_one_right = m.add_state()
    go_one_left = m.add_state()
    put_ampersand_at_the_end_state = m.add_state()
    go_back_loop_state = m.add_state()

    m.add_transition(put_first_hashtag_at_end_state, go_one_right, "_", HASH_TAG, "R")
    m.add_transition(go_one_right, put_ampersand_at_the_end_state, "_", dot_version_of["_"], "R")
    m.add_transition(put_ampersand_at_the_end_state, go_one_left, "_", AMPERSAND_SIGN, "L")
    m.add_transition(go_one_left, go_back_loop_state, dot_version_of["_"], dot_version_of["_"], "L")
    for ch in ["0", "1", HASH_TAG]:
        m.add_transition(go_back_loop_state, go_back_loop_state, ch, ch, "L")

    return go_back_loop_state


def convert_to_single_tape():
    inputs = []
    num_states = int(input())

    BASE_STATE_FIRST_INDEX = 8

    #Shift start should act as the TM begin state
    shift_end = add_shifting_machine()
    boundary_end = add_boundary_machine(shift_end)

    #States that are present in two tape TM
    #start from index 8
    for i in range(num_states - 1):
        shifting_machine_added_to[i + BASE_STATE_FIRST_INDEX] = False
        m.add_state()
        inputs.append(input())

    #This represents the accept state (The nth state)
    shifting_machine_added_to[num_states - 1 + BASE_STATE_FIRST_INDEX]  = True
    accept_state = m.add_state()

    m.add_transition(boundary_end, BASE_STATE_FIRST_INDEX, "_", DOLLAR_SIGN, "R")

    for i in range(num_states - 1):
        next_str = inputs[i]
        num_transitions = int(next_str[0])

        zero_loop_state = None
        one_loop_state = None
        empty_loop_state = None

        for k in range(num_transitions):
            #Current state = j
            j = k + BASE_STATE_FIRST_INDEX

            first_read_char = next_str[2 + k * 14]
            second_read_char = next_str[4 + k * 14]

            #Convert the given state index to its equvalent in our machine
            second_state_index = int(next_str[6 + k * 14]) + BASE_STATE_FIRST_INDEX 

            first_write_char = next_str[8 + k * 14]
            second_write_char = next_str[10 + k * 14]

            first_dir = next_str[12 + k * 14]
            second_dir = next_str[14 + k * 14]
            
            loop_state = None
            
            if first_read_char == "0":
                if zero_loop_state == None:
                    #print(str(zero_loop_state == None) + " " + str(j))
                    zero_loop_state = m.add_state()
                    m.add_transition(i + BASE_STATE_FIRST_INDEX, zero_loop_state, first_read_char, dot_version_of[first_read_char], "R")
                    for ch in ["0", "1", "_", HASH_TAG]:
                        m.add_transition(zero_loop_state, zero_loop_state, ch, ch, "R")
                loop_state = zero_loop_state
            elif first_read_char == "1":
                if one_loop_state == None:
                    one_loop_state = m.add_state()
                    m.add_transition(i + BASE_STATE_FIRST_INDEX, one_loop_state, first_read_char, dot_version_of[first_read_char], "R")
                    for ch in ["0", "1", "_", HASH_TAG]:
                        m.add_transition(one_loop_state, one_loop_state, ch, ch, "R")
                loop_state = one_loop_state
            else:
                if empty_loop_state == None:
                    empty_loop_state = m.add_state()
                    m.add_transition(i + BASE_STATE_FIRST_INDEX, empty_loop_state, first_read_char, dot_version_of[first_read_char], "R")
                    for ch in ["0", "1", "_", HASH_TAG]:
                        m.add_transition(empty_loop_state, empty_loop_state, ch, ch, "R")
                loop_state = empty_loop_state            

            second_tapehead_state = m.add_state()
            m.add_transition(loop_state, second_tapehead_state, dot_version_of[second_read_char], second_write_char, second_dir)

            #Shift the hashtag if at the edge
            if second_dir == "R":
                shift_ampersand_machine(second_tapehead_state)
            elif second_dir == "L":
                m.add_transition(second_tapehead_state, second_tapehead_state, HASH_TAG, HASH_TAG, "R")

            second_loop_state = m.add_state()
            for ch in ["0", "1", "_"]:
                m.add_transition(second_tapehead_state, second_loop_state, ch, dot_version_of[ch], "L")

            for ch in ["0", "1", "_", HASH_TAG]:
                m.add_transition(second_loop_state, second_loop_state, ch, ch, "L")

            m.add_transition(second_loop_state, second_state_index, dot_version_of[first_read_char], first_write_char, first_dir)

            #Shift the hashtag if at the edge
            if first_dir == "R":
                if shifting_machine_added_to[second_state_index] == False:
                    shifting_machine_added_to[second_state_index] = True
                    shifted_state = add_second_shifting_machine(second_state_index)

                    m.add_transition(shifted_state, second_state_index, "_", HASH_TAG, "L")

    m.set_accept_state(accept_state)



convert_to_single_tape()
print(m)
