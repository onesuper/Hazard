

from obj import Obj
from datapath import Datapath
from lazy import addi, add

obj = Obj()
obj.data_section = [1, 2]
obj.text_section = [addi('$t0', '$zero', 15),
                    addi('$t1', '$zero', 12),
                    add('$t2', '$t0', '$t1')]


datapath = Datapath()

datapath.memory.load(obj)

datapath.step()
