from tello import Tello
from datetime import datetime
import time
 
start_time = str(datetime.now())

tello = Tello()
is_piloting  = True

while(is_piloting):
    command = input("Enter a command : ")
    tello.send_command(command)
    if command == 'stop' :
        is_piloting = False
    
log = tello.get_log()

out = open('log/' + start_time + '.txt', 'w')
for stat in log:
    stat.print_stats()
    str = stat.return_stats()
    out.write(str)