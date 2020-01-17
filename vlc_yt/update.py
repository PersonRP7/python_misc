import os
import shutil
import requests
import sys

#A generic exception handler which wraps all 3 functions.
def exception_handler(callback):
    try:
        return callback()
    except Exception as e:
        sys.stderr.write(f"Excepted error: {e}")

#Downloads youtube.luac from vlc's github and saves it to the current directory.
def download_youtube():
    vlc = requests.get("https://raw.githubusercontent.com/videolan/vlc/master/share/lua/playlist/youtube.lua")
    with open('./youtube.luac', 'wb') as file:
        file.write(vlc.content)
        
#Removes the current youtube.luac instance.
def remove_youtube():
    os.remove("C:\\Program Files\\VideoLAN\\VLC\\lua\\playlist\\youtube.luac")

#Copies the downloaded youtube.luac to vlc's directory.
def update_youtube():
    vlc_directory = "C:\\Program Files\\VideoLAN\\VLC\\lua\\playlist"
    shutil.copy("./youtube.luac", vlc_directory)

functions = [
    download_youtube,
    remove_youtube,
    update_youtube
]

def runner():
    for function in functions:
        exception_handler(function)

if __name__ == "__main__":
    runner()