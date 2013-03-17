
# execuatble file is no longer a block of binaries
# it is represented by two arrays - data and text of 32-bit words
# just for readablity!
# it can be dumped into memory by the loader

class Obj(object):
    def __init__(self, data_section=[], text_section=[], entry=0x1000000):
        self.data_section = data_section
        self.text_section = text_section
        self.entry = entry  # entry point of exe

    def _prettify_data(self):
        data_string = ''
        for i, d in enumerate(self.data_section):
            data_string += "  {0}:  {1:x}\n".format(hex(i), d)
        return data_string

    def _prettify_text(self):
        text_string = ''
        for i, t in enumerate(self.text_section):
            text_string += "  {0}:  {1:x}\n".format(i, t)
        return text_string

    def __repr__(self):
        return '<.data>:\n' + self._prettify_data() + '\n<.text>: \n' + self._prettify_text()
