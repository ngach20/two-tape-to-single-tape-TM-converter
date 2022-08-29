class Transition:
    _start_state = None
    _end_state = None

    _trans_char = ""
    _write_char = ""
    _dir = ""

    def __init__(self, start_state, end_state, trans_char, write_char, dir):
        self._start_state = start_state
        self._end_state = end_state
        self._trans_char = trans_char
        self._write_char = write_char
        self._dir = dir

    def get_start_state(self):
        return self._start_state

    def get_end_state(self):
        return self._end_state

    def get_trans_char(self) -> str:
        return self._trans_char

    def get_write_char(self) -> str:
        return self._write_char

    def get_dir(self) -> str:
        return self._dir

    def __str__(self) -> str:
        final_str = (self._trans_char + " ")
        final_str += (str(self._end_state.get_state_num()) + " ")
        final_str += (self._write_char + " ")
        final_str += str(self._dir)
        return final_str
