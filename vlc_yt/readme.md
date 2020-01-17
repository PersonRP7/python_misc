# Update script for VLC youtube network streaming capability

Description:
    Due to youtube's persistent URL changes, VLC's youtube network streaming capability is
    negatively impacted on a periodic basis. While the VLC team rectifies these changes by modifying their internal streaming configuration files (youtube.luac in this case), they do not however ship these files as part of their regular update schedule. 

## Usage:

```
python update.py
```

Requirements:
A python interpreter 3.6 or above is required due to this script's reliance on 
f - strings.

External resources:
[youtube.luac file](https://raw.githubusercontent.com/videolan/vlc/master/share/lua/playlist/youtube.lua)