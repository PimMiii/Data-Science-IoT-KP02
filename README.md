# Data-Science-IoT-KP02
Data-Science-IoT Keuzevak HR periode 02 2022.

# PRiTC
***P***ositive ***R***e***i***nforcement upon ***T***ask ***C***ompletion

## Problem
I seem to have a pattern of procrastination, which sooner rather than later will come to haunt me.

Maybe it already has, seeing how my first idea for a project was a 'smart' (read ring-like) doorbell,
but knowing virtually nothing about image processing makes that seem like a daunting task,
especially if it needs to be finished before the deadline.  

## Goal of the Project
So on to the current idea: **PRiTC**.  
Positive Reinforcement upon Task Completion, a discord bot sending positive and encouraging messages to myself.  
The idea sounds simple enough yet effective.  
The Internet-of-Things application consists of a RPi3a+, 3 buttons, and a DHT11 (temp and humidity) sensor.  



## Thingspeak

Channel consists of 6 fields:
1. Completion (is task completed: 0 = cancelled/not completed, 1 = completed)
2. Start time (timestamp of the task starting time)
3. End time (timestamp of the task ending time)
4. Duration (time it took for task to be completed in seconds)
5. Temperature (Temperature reported by DHT11, Room Temperatre in °C)
6. Humidity (Humidity reported by DHT11)

### install requirements 
to install the required modules on RPi:  
``` pip install -r requirements.txt ```