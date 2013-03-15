


# execuatble file is no longer a block of binaries
# it is represented by two arrays - data and text of 32-bit words
# just for readablity!
# it can be dumped into memory by the loader

class EXE(object):
    def __init__(self, data_section, text_section, entry=0):
        self.data_section = data_section
        self.text_section = text_section
        self.entry = entry

    def __repr__(self):
        return
