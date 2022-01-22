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
The idea sounds simple enough yet effective. A physical panel on my desk, with a couple buttons ready to press to signal
start of task and task finished or cancelled. These buttons would be hooked up to a RPi 3a+. On a button press a task
will be started, and an internal timer will run, then a press on the button for completing the task would log the task
as completed, the other button would cancel the task. On task completion the task data (date, and time to complete)
will be send over the internet to ThingSpeak and a discord bot running on my desktop would receive this data through the
IoT middleware platform prompting the bot to send a randomly selected positive reinforcement.  

### Possible extension
The gathered data could be extended to include light-levels (using LDRs in the circuit), and perhaps even sound-levels. 

## Thingspeak

Channel expects 7 fields:
1. Completion (is task completed: 0 = cancelled/not completed, 1 = completed)
2. Start time (timestamp of the task starting time)
3. End time (timestamp of the task ending time)
4. Duration (time it took for task to be completed in seconds)
5. lightlevel start (lightlevel value at start of task)
6. lightlevel end (lightlevel value at end of task)
7. lightlevel average (average of continuous lightlevel measures taken during task)

