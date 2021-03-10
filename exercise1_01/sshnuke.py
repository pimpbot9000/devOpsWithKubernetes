import random
import time
import string
import datetime
import os

class App():
    def __init__(self, N, delay):
        self.random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=N))
        self.delay = delay

    def start_timer(self):
        while True:
            dt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            output_str = 'echo {dt}: {random_str}'.format(dt=dt, random_str=self.random_str)
            #print(output_str)
            os.system(output_str)
            time.sleep(5)

if __name__ == "__main__":
    app = App(N=10, delay=5)
    app.start_timer()

