import edgeLink
import validators

while True:
    
    print('(1) Youtube\n(2) Facebook\n(3) Twitter\n(4) Instagram')
    link = input("Choose the website you'd like to open or type in the link directly: ")
    if link == '1':
        edgeLink.edge(edgeLink.websites['youtube'])
    elif link == '2':
        edgeLink.edge(edgeLink.websites['facebook'])
    elif link == '3':
        edgeLink.edge(edgeLink.websites['twitter'])
    elif link == '4':
        edgeLink.edge(edgeLink.websites['instagram'])
        
    else:
        if(validators.url(link)):
            edgeLink.edge(link)
        else:
            print("Invalid URL.")
    
    print('Would you like to open another website?\nY/N?\t')
    checker = input()
    if(checker.lower() != 'y'):
        break