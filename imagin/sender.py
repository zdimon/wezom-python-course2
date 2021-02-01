import socketio
import time
from datetime import datetime
from imagin.settings import BASE_DIR
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess, time 
import os
import sys
import signal
import psutil
json_path = f'{BASE_DIR}/static/data.json'      

mgr = socketio.RedisManager('redis://redis:6379/0', write_only=True)
  

pid = os.getpid()

print('Starting sender server with pid', pid)


class EditHandler(FileSystemEventHandler): 
   

    def on_modified(self, event): 
        print('Restarting') 
        
        #time.sleep(1)  
        p = psutil.Process(pid) 
        
        subprocess.run('python3 sender.py', shell=True)   
        time.sleep(1)
        p.terminate()  
        #os.kill(os.getppid(), signal.SIGTERM) 
        # subprocess.run('python3 sender.py', shell=True)   
        # time.sleep(0.2)  
        # quit()   
  
 
# observer = Observer()
# observer.schedule(EditHandler(), '.', recursive=True)
# observer.start()  
    
while True: 
    time.sleep(2)    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    with open(json_path,'r') as file:
        json_data = json.loads(file.read())
    mgr.emit('ping', data={'time': current_time,'state': json_data})
    #print(current_time,'sending')