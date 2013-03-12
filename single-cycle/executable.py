


# execuatble file is no longer a block of binaries
# it is represented by two arrays - data and text of 32-bit words
# just for readablity!
# it can be dumped into memory by the loader

class EXE(object):
    def __init__(self, data, text):
        self.data = data
        self.text = text
