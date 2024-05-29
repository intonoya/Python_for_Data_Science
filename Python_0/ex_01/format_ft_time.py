import time
import datetime

current_time = time.time()
c_s = time.time()  # current time in seconds
current_time = datetime.datetime.fromtimestamp(current_time)
scientific_notation = "{:e}".format(c_s)
msg = "Seconds since " + current_time.strftime('%B %d, %Y:') + " " + str(c_s)
print(msg + " or " + scientific_notation + " in scientific notation")
print(current_time.strftime('%b %Y %d %H:%M:%S'))
