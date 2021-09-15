#!/usr/bin/python3
import schedule
import time
from plyer import notification
import os
from systemd import journal

system_audio_player = 'ogg123' #sudo apt install vorbis-tools for ogg123
audio_player_flags = ''
audio_file1 = "eye_care_audio/complete.oga"
audio_file2 = "eye_care_audio/message.oga"

def func():
    notification.notify(title= "20-20-20 Rule",
                    message= "Give break to eyes. Look away for 20 sec",
                    timeout= 25,
                    toast=False,
                    app_name = 'Eye Care')
    try:
        os.system(system_audio_player+' '+audio_player_flags+' '+audio_file1)
        time.sleep(24)
        os.system(system_audio_player+' '+audio_player_flags+' '+audio_file2)
    except Exeception as e:
        journal.send(e.args)



schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)

