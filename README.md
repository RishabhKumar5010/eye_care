# Eye Care

Too much strain in your eyes while in front of your screen?

Need a tool that reminds you of the [20-20-20 rule](https://www.medicalnewstoday.com/articles/321536#supporting-evidence)?

This repo may interest you.


## 20-20-20 Rule

Staring at a screen for prolonged periods can strain eyes as they have to lock on a constant focal distance for prolonged time. So one could 
practise the 20-20-20 rule which says "For every 20 minutes spent looking at a screen, you take a 20 second break and look at something 20+ feet away"

## What does the Script do

Tested on my Ubuntu system, this python script will trigger a notification with sound cues that prompts you a reminder to look away from the screen for
20 secs. Focus on something that is atleast 20 feet away. This notification will popup every 20 min.

20-20-20 is a generalised rule for average person. Everyone can have their own preferences about when to take a break and for how long.

Edit the script parameters to adjust it to your needs.


## Dependencies

* Plyer 2.0.0  
`pip3 install plyer`

* Schedule 1.1.0  
`pip3 install schedule`

* A native (CLI) music player\
I have used ogg123. If you have something else edit the script's global parameters accordingly.\
To get ogg123 on ubuntu\
`sudo apt install vorbis-tools`

## Adding in Startup Applications:

I am using KDE desktop on ubuntu and there is a GUI app called Autostart which can be used to add a script as a startup application, so that the script doesn't need to be manually run after each system boot. You can search for steps to add a script to startup apps respective to your platform.


## Debugging

Errors in the program related to the actual working of the notification module are recorded
into the journaling program on your system. On my ubuntu system the error generated are reflected
into `journalctl`. You can use this CLI utility or a GUI app like KSystemLog to view errors.

If the program crashes due to unhandled errors, you would know this by checking if the program
is running in the background. On my ubuntu system I can use `ps ax | grep python` to check
if the program (eye.py) is active in background or not.
One can also use `top` for this purpose.
