import webbrowser

facebook_link = "https://www.facebook.com/"
#youtube_link = "https://www.youtube.com/"
#instagram_link = "https://www.instagram.com/"
#twitter_link = "https://www.twitter.com/"

def edge(link):
    
    edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s'
    webbrowser.get(edge_path).open(link)