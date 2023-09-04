import webbrowser

websites = {
    "facebook" : "https://www.facebook.com/",
    "youtube" : "https://www.youtube.com/",
    "instagram" : "https://www.instagram.com/",
    "twitter" : "https://www.twitter.com/"
}
  
def edge(link):
   webbrowser.get("/opt/microsoft/msedge/msedge %s").open(link)