__author__ = 'viettran'
from braille import dictionary


class DecodeBraille(object):
    def __init__(self, file):
        self.input = open(file)
        self.arrayLine = []

    # read one-line first
    def decode(self):
        text = self.input.read()
        i = 0
        for line in text.split('\n'):
            i += 1
            # create array of line consist of (len(line)+1)/3 = number of character
            list_part_character = line.split(' ')
            for index in range((len(line) + 1) / 3):
                if len(self.arrayLine) < ((len(line) + 1 )/ 3):
                    self.arrayLine.append(list_part_character[index])
                else:
                    self.arrayLine[index] += list_part_character[index]
        # read
        # read 3 line complete a line in braille
        if i == 3:
            line_out = ''
            for character in self.arrayLine:
                line_out += dictionary[character]
            print line_out
            print '\n'


decoder = DecodeBraille('input')
decoder.decode()
