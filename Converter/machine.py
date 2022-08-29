from state import State
from transition import Transition

class Machine:
    _num_states = 0
    _start_state = None
    _end_state = None
    _accept_state = -1

    _states = []


    def __init__(self):
        self._states = []   

    def add_state(self):
        new_state = State(self._num_states)

        if self._num_states == 0:
            self._start_state = new_state
        
        self._end_state = new_state
        self._states.append(new_state)
        self._num_states += 1
        return self._num_states - 1

    #def get_state(self, index : int) -> State:
    #    return self._states[index]

    def add_transition(self, start_state : int, end_state : int, trans_char : str, write_char : str, dir : str):
        new_transition = Transition(self._states[start_state], self._states[end_state], trans_char, write_char, dir)
        self._states[start_state].add_transition(new_transition)

    def set_accept_state(self, state_num : int):
        self._states[state_num].set_state_num(len(self._states) - 1)
        for st in self._states[state_num + 1:]:
            st.set_state_num(st.get_state_num() - 1)
        self._accept_state = len(self._states) - 1

    #def get_num_states(self):
    #    return self._num_states

    #def contains_state(self, state_num):
    #    return self._num_states >= state_num

    def __str__(self) -> str:
        final_str = str(self._num_states) + "\n"
        for st in self._states:
            if st.get_state_num() == self._accept_state:
                continue
            final_str += (str(st) + "\n")
        
        #if self._accept_state != -1:
        #   final_str += (str(self._states[self._accept_state]) + "\n")
        
        return final_str
