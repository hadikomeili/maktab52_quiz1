import jdatetime
import os
import time


file_path = 'p2.txt'

class Timestampopen:

    def __init__(self, file_path: str, mode: str = 'r'):
        self.file_path = file_path
        self.mode = mode
        self.s_time = 0
        self.e_time = 0
        assert self.mode in ('r', 'rb', 'r+', 'w', 'wb', 'w+', 'wb+', 'a', 'ab', 'a+', 'ab+'), 'invalid input!!!'
        assert os.path.isdir(self.file_path) or os.path.isfile(self.file_path), 'invalid input!!!'

    def read(self):
        if self.mode == 'r' or 'a' or 'w' or 'r+' or 'w+' or 'a+':
            with open(self.file_path, 'r') as f:
                res = f.read()
        elif self.mode == ('rb' or 'wb' or 'wb+' or 'ab' or 'ab+'):
            with open(self.file_path, 'rb') as f:
                res = f.read()
        return res

    def write(self, text: str):
        with open(self.file_path, self.mode) as f:
            f.write(text)

    def __enter__(self):
        self.s_time = jdatetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.e_time = jdatetime.datetime.now()
        open_content = 'open jalali time stamp: ' + self.s_time.strftime("%a, %d %b %Y %H:%M:%S")+ '\n'
        close_content = 'close jalali time stamp: ' + self.e_time.strftime("%a, %d %b %Y %H:%M:%S")
        content = open_content + close_content
        with open(file_path, 'a') as new_f:
            time_stamp_content = new_f.write(content)


        return True

with Timestampopen(file_path, 'r') as f:
    time.sleep(5)
    f.read()