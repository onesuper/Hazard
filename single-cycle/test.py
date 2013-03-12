

from executable import EXE
from loader import Loader
from memory import Memory



exe = EXE([0b00000000111111110000000011111111],
          [0b11111111000000001111111100000000])


# a memory loaded with data and code
memory = Loader().load(exe, Memory())


datapath = Datapath(memory)
