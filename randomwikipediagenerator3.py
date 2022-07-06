import requests
import webbrowser

blocked_words = ["Seth","Rose","Olive","Mildred","Robert","Gad","Saleh","Eric","Dickens","Racheal"]

def exclude_articles():
    for i in range(0,5):
        valid = False
        while(not valid):  
        #get the random form wikipedia article
            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
            json = response.json()

            summary = json['extract']
            if not any(c in summary for c in blocked_words):
                valid = True

                #get the URL to open in browser
                title = json['title']
                #remove non-ascii charcters
                title = "".join(i for i in title if ord(i)<128)
                url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")
                #open the url
                webbrowser.open_new_tab(url)

exclude_articles()     

wanted_words = ["Seth","Rose","Olive","Mildred","Robert","Gad","Saleh","Eric","Dickens","Racheal"]

def include_articles():
    for i in range(0,5):
        valid = False
        while(not valid):  
        #get the random form wikipedia article
            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
            json = response.json()

            summary = json['extract']
            if any(c in summary for c in wanted_words):
                valid = True
                #get the URL to open in browser
                title = json['title']
                #remove non-ascii charcters
                title = "".join(i for i in title if ord(i)<128)
                url = 'https://en.wikipedia.org/wiki/' + title.replace(" ","_")
                #open the url
                webbrowser.open_new_tab(url)

include_articles()  

def scan_full_article():
    for i in range(0,5):
        valid = False
        while(not valid):
            #get info of a random wikipedia article
            response = requests.get('https://en.wikipedia.org/api/rest_v1/page/random/summary')
            html = response.text
            
            if any(
                

