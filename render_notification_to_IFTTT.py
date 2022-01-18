#!/usr/bin/env python

"""
    README
    This script send it to a IFTTT webhook, and is triggered by render job in the deliver page.
    It needs to be placed in the following OS specific directory:
    Mac OS X:   ~/Library/Application Support/Blackmagic Design/DaVinci Resolve/Fusion/Scripts/Deliver
    Windows:    %APPDATA%\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Deliver\
    Linux:      /opt/resolve/Fusion/Scripts/Deliver/   (or /home/resolve/Fusion/Scripts/Deliver depending on installation)


  
"""
import requests
import json

if __name__ == '__main__':
    webhook_url = "https://maker.ifttt.com/trigger/Resolve_Render_Job/with/key/{your_key}" # webhook url
    message = "Resolve render job is completed!" # webhook message
    requests.post(webhook_url, data=json.dumps({'text': message}))
