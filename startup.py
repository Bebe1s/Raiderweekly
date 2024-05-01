import subprocess
import time

sub1 = "rm -fR Raiderweekly"
sub2 = "git clone https://github.com/Bebe1s/Raiderweekly.git"
sub3 = "vlc --fullscreen --no-audio --no-video-title-show --loop /home/raiderTVs/Raiderweekly/Video.mp4"
sub4 = "sudo reboot"

current_time = time.strftime("%H:%M:%S")

def getime():
    if current_time is "0:0:0" or "12:0:0":
        subprocess.run(sub4, shell=True)
    else:
        getime()

subprocess.run(sub1, shell=True)
subprocess.run(sub2, shell=True)
subprocess.run(sub3, shell=True)
getime()