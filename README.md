# Two tape to single tape Turing Machine converter.
University project for Theoretical computer science.

# Convert.py Usage
- Integer n for number of states.
- (n-1) lines, each line corresponding to each state:
  - m (a0 b0 s a1 b1 dir1 dir2):
   - m : number of transitions from the given state.
   - for one transition:
    - a0, b0 : symbols to read from each tape.
    - s : state to transition to.
    - a1, b1 : syblos to write on each tape.
    - dir1, dir2 : directions for each tape (either 'L' or 'R').

# Symulate.py Usage
Simulate a single tape turing machine.
- Integer n for number of states.
- (n-1) lines, each line corresponding to each state:
  - m (a0 s a1 dir):
   - m : number of transitions from the given state.
   - for one transition:
    - a0 : symbol to read.
    - s : state to transition to.
    - a1 : symbol to write.
    - dir : direction for the tape.

