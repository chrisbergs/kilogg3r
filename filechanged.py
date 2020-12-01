import os
import sys
import time

class FileChanger(object):
    def __init__(self):
        self._cached_stamp = 0
        self.user = "crippa"
        self.filename = "log"
        self.path = f"/home/{self.user}/logs/kilogg3r/"
        self.changed = False
        self.stamp = os.stat(self.path + self.filename).st_mtime
        self._cached_stamp = self.stamp
        self.sleep = 5

    def watch(self):
        stamp = os.stat(self.path + self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            print('change')

try:
    watcher = FileChanger()
    watcher.watch()
    while True:
        time.sleep(watcher.sleep)
        watcher.watch()
        
except KeyboardInterrupt:
    print('\nDone')
except:
    print(f'Unhandled error: {sys.exc_info()[0]}') 