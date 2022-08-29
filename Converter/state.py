from transition import Transition

class State:
    _state_num = 0

    _num_transitions = 0
    _transitions = []


    def __init__(self, num):
        self._state_num = num
        self._transitions = []

    def __repr__(self):
        return self._state_num

    def transition_exists(self, read_char):
        for tr in self._transitions:
            if tr.get_trans_char() == read_char:
                return True
        return False

    def add_transition(self, transition: Transition):
        if self.transition_exists(transition.get_trans_char()):
            print("Machine just became non-deterministic while making transition from: ")
            print(str(transition.get_start_state()) + " to " + str(transition.get_end_state()))


        self._transitions.append(transition)
        self._num_transitions += 1

    def get_state_num(self):
        return self._state_num

    def set_state_num(self, state_num):
        self._state_num = state_num

    def get_num_transitions(self):
        return self._transitions

    def __str__(self) -> str:
        #final_str = "State num is: " + str(self._state_num) + " __ " + str(self._num_transitions) + " "
        final_str = str(self._num_transitions) + " "
        for tr in self._transitions:
            final_str += (str(tr) + " ") 
        return final_str 
            
