# --/ We're using WSL so the webbrowser module wouldn't work to launch the default browser on the host system /--
#import webbrowser

#import webbrowser

# Instead, we'll use subprocess to utilize wslview

import subprocess

websites = {
    "facebook" : "https://www.facebook.com/",
    "youtube" : "https://www.youtube.com/",
    "instagram" : "https://www.instagram.com/",
    "twitter" : "https://www.twitter.com/"
}

# WSL

def edge(link):
    subprocess.run(["wslview", link])
    

# Non-WSL    
#def edge(link):
#    webbrowser.get("C:/Program Files/Google/Chrome/Application/chrome.exe %s").open(link)