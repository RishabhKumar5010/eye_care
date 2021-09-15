#!/usr/bin/python3
import schedule
import time
from plyer import notification
import os
from systemd import journal

#### global config #####
system_audio_player = 'ogg123' #sudo apt install vorbis-tools for ogg123
audio_player_flags = ''
audio_file1 = "~/scripts/eye_care/eye_care_audio/complete.oga"
audio_file2 = "~/scripts/eye_care/eye_care_audio/message.oga"

repeat_mins = 25 # one work session or show the popup every x mins
look_away_secs = 25 # hold the popup on the screen for x secs while you look away

########################

def func():
    try:
        notification.notify(title= "20-20-20 Rule",
                    message= "Give break to eyes. Look away for 20 sec",
                    timeout= look_away_secs,
                    toast=False,
                    app_name = 'Eye Care')
        os.system(system_audio_player+' '+audio_player_flags+' '+audio_file1)
        time.sleep(look_away_secs - 1)
        os.system(system_audio_player+' '+audio_player_flags+' '+audio_file2)
    except Exeception as e:
        journal.send(e.args)



schedule.every(repeat_mins).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)

