
# Little-endian type assumed
# The memory is intented to provide 4G addressing space
# However, to save place, here I only use two 4K-size-arrays to store data and text 
# If an instruction tries to address out of the two arrays, the program will rasie an execption



from exception import MemoryException


text_start = 0x00400000
data_start = 0x10000000


class Memory(object):


    def __init__(self):
        self.text = [0] * 4096
        self.data = [0] * 4096
        
    def _read(self, addr):
        if text_start <= addr <= text_start + 4096:
            return self.text[addr-text_start]
        elif data_start <= addr <= data_start + 4096:
            return self.data[addr-data_start]
        else:
            raise MemoryException('segment fault')

    def _write(self, addr, byte):
        if text_start <= addr <= text_start + 4096:
            self.text[addr-text_start] = byte
        elif data_start <= addr <= data_start + 4096:
            self.data[addr-data_start] = byte
        else:
            raise MemoryException('segment fault')

    def show_data(self, start=0, end=15):
        return self.data[start:end]

    def show_text(self, start=0, end=15):
        return self.text[start:end]

    def getByte(self, addr):
        return self._read(addr)

    def setByte(self, addr, value):
        self._write(addr, value)

    def getWord(self, addr):
        return self._read(addr) + (self._read(addr+1) << 8) + (self._read(addr+2) << 16) + (self._read(addr+3) << 24)

    def setWord(self, addr, value):
        self._write(addr, value & 0x000000ff)
        self._write(addr+1, (value & 0x0000ff00) >> 8)
        self._write(addr+2, (value & 0x00ff0000) >> 16)
        self._write(addr+3, (value & 0xff000000) >> 24)



    # load the obj code into memory
    def load(self, obj):
        data, text =  obj.data_section, obj.text_section
        for i in range(len(data)):
            self.setWord(data_start+i*4, data[i])
        for i in range(len(text)):
            self.setWord(text_start+i*4, text[i])

