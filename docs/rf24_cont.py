# use the serial class
# it also has the serial funtion
# command string is converted to 30 bytes for RF Module and send it

from serial import Serial

class rf24_dongle():

    ser_port = None

    def __init__(self,**kwargs):
        pass

    def init(self, port):
        self.ser_port = Serial(port,9600, timeout= 1)

    def do_at(self):
        self.ser_port.write(bytes('AT?', encoding='ascii'))
        msg = bytearray()
        while True:
            ch = self.ser_port.read()
            if len(ch) == 0:
                break
            msg.append(ch[0])
        msg_bytes = bytes(msg)
        str = msg_bytes.decode(encoding='ISO-8859-1')
        print(str)

    def write(self, str):
        send_msg = bytearray(32)
        in_str = bytearray(str,encoding='utf8')

        send_msg[0] = len(str)
        for i,v in enumerate(in_str):
            send_msg[i+1] = v
        self.ser_port.write(bytes(send_msg))

    def close(self):
        self.ser_port.close()

