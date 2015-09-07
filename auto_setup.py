import urllib.request
import time
import sys
import subprocess
from serverbrowser import open_browser

print("Trying to download phaser.min.js.")
file = urllib.request.urlopen('https://github.com/photonstorm/phaser/releases/download/v2.4.3/phaser.min.js')
with open('phaser.min.js', 'b+w') as phaser:
    phaser.write(file.read())
    print("Phaser downloaded successfully!")
    print("Starting server setup")
    open_browser()



    
