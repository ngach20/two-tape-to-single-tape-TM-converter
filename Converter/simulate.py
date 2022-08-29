num_states = 0
transitions = {}
tape = ""

STEP_LENGTH = 4

num_states = int(input())

def process_machine_string():

    for i in range(num_states - 1):
        cur_trans = input()
        num_trans = int(cur_trans[0])

        cur_dict = {}
        for j in range(num_trans):
            sp = cur_trans.split()
            #print(sp)
            next_state = int(sp[2 + j * STEP_LENGTH])
            read_ch = sp[1 + j * STEP_LENGTH]
            write_ch = sp[3 + j * STEP_LENGTH]
            dir = sp[4 + j * STEP_LENGTH]
            
            cur_dict[read_ch] = (next_state, write_ch, dir)
        
        transitions[i] = cur_dict
            

#Read all transitions
#Save them in a dictionary
#Format:     {cur_state : DICT{ read_char : (next_state, write_char, direction), read_char2 : ... }, cur_state2 : ... } 
process_machine_string()
tape = input()

cur_state = 0
idx = 0
while True:
    cur_char = tape[idx]

    if cur_char in transitions[cur_state]:
        (next_state, write_ch, dir) = transitions[cur_state][cur_char]
        
        tape = tape[ :idx] + write_ch + tape[idx + 1: ]

        if dir == "R":
            idx += 1
            if idx == len(tape):
              tape = tape + "_"
        else:
            idx -= 1

        print(next_state)
        if next_state == num_states - 1:
            break

        cur_state = next_state
    else:
        print(-1)
        break


