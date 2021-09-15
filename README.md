# Eye Care

Too much strain in your eyes while in front of your screen?

Need a tool that reminds you of the [20-20-20 rule](https://www.medicalnewstoday.com/articles/321536#supporting-evidence)?

This repo may interest you.


## 20-20-20 Rule

Staring at a screen for prolonged periods can strain eyes as they have to lock on a focus for prolonged time. So one could 
practise the 20-20-20 rule which says "For every 20 minutes spent looking at a screen, you take a 20 second break and look at something 20+ feet away"

## What does the Script do

Tested in my linux machine this python script will trigger a notification with sound cues that prompts you a reminder to look away from the screen for
20 secs. While looking away look at something atleast 20feet away. This notification will popup every 20min.

However 20-20-20 is a generalised rule for average person. Everyone can have their own preferences about when to take a break and for how long.
I have read somewhere to keep these break atleast once every 30min, but not sure of the base for this recommendation.

Edit the script parameters to adjust it to your needs.


## Dependencies

* Plyer 2.0.0  
`pip3 install plyer`

* Schedule 1.1.0
`pip3 install schedule`

* A native (CLI) music player\
I have used ogg123 however if you have something else edit the script's global parameters accordingly\
To get ogg123 on ubuntu\
`sudo apt install vorbis-tools`

## Adding in Startup Applications:
