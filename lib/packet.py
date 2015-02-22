from utilities import *

class Packet(object):
    def __init__(self, ords):
        self.data_type = ords[0]
        self.cls = ords[2]
        self.command = ords[3]
        self.payload = multichr(ords[4:])

    def __repr__(self):
        return 'Packet(%02X, %02X, %02X, [%s])' % \
            (self.data_type, self.cls, self.command,
             ' '.join('%02X' % b for b in multiord(self.payload)))