
# Little-endian type assumed
# The memory is intented to provide 4G addressing space
# However, to save place, here I only use two 4K-size-arrays to store data and text 
# If an instruction tries to address out of the two arrays, the program will rasie an execption



from exception import MemoryException


class Memory(object):
    def __init__(self, text_segment=0x00400000, data_segment=0x10000000):
        self.text_segment = text_segment
        self.data_segment = data_segment
        self.text = [0] * 4096
        self.data = [0] * 4096
        
    def _read(self, addr):
        if self.text_segment <= addr <= self.text_segment + 4096:
            return self.text[addr-self.text_segment]
        elif self.data_segment <= addr <= self.data_segment + 4096:
            return self.data[addr-self.data_segment]
        else:
            raise MemoryException('segment fault')

    def _write(self, addr, byte):
        if self.text_segment <= addr <= self.text_segment + 4096:
            self.text[addr-self.text_segment] = byte
        elif self.data_segment <= addr <= self.data_segment + 4096:
            self.data[addr-self.data_segment] = byte
        else:
            raise MemoryException('segment fault')

    def getByte(self, addr):
        return self._read(addr)

    def setByte(self, addr, value):
        self._write(addr, value)

    def getWord(self, addr):
        return self._read(addr) + (self._read(addr+1)<<8) + (self._read(addr+2)<<16) + (self._read(addr+3)<<24)
