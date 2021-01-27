import requests
import time
import bs4
    
startTime = time.time()

for i in range(1,1000):
    res = requests.get('http://localhost:8080')

executionTime = (time.time() - startTime)
print('Execution time in seconds: ' + str(executionTime))