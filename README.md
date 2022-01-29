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
Data collected includes Humidity, Room temperature, Start and end time for a task, it's completion status
(finished or cancelled) and it's duration in seconds.    
Data gets send to ThingSpeak, from where the Discord-bot can read
it through the ThingSpeak API. Data on ThingSpeak can be used to visualize correlation between temp and humidity
(comes pre-configured through MATLAB), but also in the future with enough data-points collected maybe find a pattern between
room temp/humidity and my ability to finish tasks.    
In other words to visualize at what room temp/humidity I am most productive.
  
In terms of learning goals, I'd say becoming more comfortable with the hardware side of things.  
But also getting more comfortable navigating the commandline by using the pi through SSH/ the commandline.  
Getting to play around with a IoT/data science pipeline is a welcome addition as well, and a new experience for sure.  
Furthermore, general coding/programming experience is always welcome.  
And finally, personal-growth/ learning would come from the overall end goal of the project, the positive reinforcement, and learning
to be more positive towards myself.
  
  

## The Project

### Required hardware
- Raspberry Pi 3a+ or newer
- DHT11 sensor
- Breadboard
- Du Pont male-female jumper wires
- 2 (or 3) push buttons

### Thingspeak channel
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

