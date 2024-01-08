# import the time module 
import time 
  
# define the countdown func. 
def countdown(n): 
    
    while n: 
        mins, secs = divmod(n, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        n -= 1
      
    print('Times up!') 
  
  
# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(n)) 