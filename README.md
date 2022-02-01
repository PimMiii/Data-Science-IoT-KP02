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

### Pipeline
<img src="img/IoT Pipeline.jpg"/>

### Required hardware
- Raspberry Pi 3a+ or newer
- DHT11 sensor
- Breadboard
- Du Pont male-female jumper wires
- 2 (or 3) push buttons

### Thingspeak channel
Channel consists of 6 fields:
1. `task_status` (is task completed: 0 = cancelled/not completed, 1 = completed)
2. `task_start` (timestamp of the task starting time)
3. `task_end` (timestamp of the task ending time)
4. `task_duration` (time it took for task to be completed in seconds)
5. `temp` (Temperature reported by DHT11, Room Temperature in °C)
6. `humidity` (Humidity reported by DHT11)

### install requirements 
to install the required modules on RPi:  
```$ pip install -r requirements.txt ```

## The Prototype

The prototype is nothing more than a bunch of wires, and 2 small cardboard boxes the components arrived in by mail.  
Held together by (packing) tape, with some holes cut into the cardboard for ventilation/ wires.  
And finally a hole on the top covered up with the same tape to create some sort of 'window' to peer into the innerwirings.  

### pictures
<img src="img/prototype/prototype01.jpg"/>
<small> The on/off button LEDs still worked here. I think i ended up shorting them out or something. Oops</small>
<img src="img/prototype/prototype04.jpg">
<img src="img/prototype/prototype03.jpg"/>
<small> there's a lot of wires coming from the buttons. the right most button is the on/off button.</small>
<img src="img/prototype/prototype08.jpg">
<img src="img/prototype/prototype05.jpg">
<img src="img/prototype/prototype07.jpg">
<img src="img/prototype/prototype06.jpg">
<img src="img/prototype/prototype02.jpg">