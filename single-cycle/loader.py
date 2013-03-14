



class Loader(object):
    def load(self, executable, memory):
        data, text =  executable.data, executable.text
        for i in range(len(data)):
            memory.setWord(memory.data_segment+i*4, data[i])
        for i in range(len(text)):
            memory.setWord(memory.text_segment+i*4, text[i])
        return memory
    
