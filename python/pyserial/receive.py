# uart_controller.py 接收狀態機

import time
import threading

import serial


class UartController(threading.Thread):
    def __init__(self, received_handler=None):
        threading.Thread.__init__(self)
        self.ser = serial.Serial(port='COM30', baudrate=115200, timeout=1)
        self.received_handler = received_handler

    def run(self):
        rxlen = 0
        mode = 'idle'

        checktime = time.time()
        while True:
            if mode == 'idle':
                if self.ser.in_waiting > rxlen:
                    rxlen = self.ser.in_waiting
                    checktime = time.time()
                    mode = 'busy'

            elif mode == 'busy':
                TIMEOUT_CONDITION = 0.02
                timeeclipse = time.time() - checktime
                if timeeclipse > TIMEOUT_CONDITION:
                    mode = 'timeout'
                else:
                    if self.ser.in_waiting > rxlen:
                        rxlen = self.ser.in_waiting
                        checktime = time.time()

            elif mode == 'timeout':
                rxpacket = self.ser.read(self.ser.in_waiting)
                if self.received_handler:
                    self.received_handler(rxpacket)

                mode = 'idle'
                rxlen = 0
            time.sleep(0.01)

    def write_raw_packet(self, pkt):
        self.ser.reset_output_buffer()
        self.ser.reset_input_buffer()
        self.ser.write(pkt)
        self.ser.flush()


def dumphex(pkt):
    result = ' '.join(['{:02x}'.format(b) for b in pkt])  # debug
    print('[32m{}[m'.format(result))


if __name__ == '__main__':
    uctl = UartController(dumphex)
    uctl.start()