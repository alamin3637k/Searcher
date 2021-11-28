import webbrowser
import pywhatkit
import wikipedia

class sercher:
    def __init__(self):
        pass

    def yt_search(self, search):
        webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={search}")
    
    def google_search(self, search):
        webbrowser.open_new_tab(f"https://www.google.com/search?q={search}")
    
    def bing_search(self, search):
        webbrowser.open_new_tab(f"https://www.bing.com/search?q={search}")
    
    def duck_search(self, search):
        webbrowser.open_new_tab(f"https://duckduckgo.com/?q={search}")
    
    def yahoo_search(self, search):
        webbrowser.open_new_tab(f"https://search.yahoo.com/search?p={search}")
    
    def ask_search(self, search):
        webbrowser.open_new_tab(f"https://www.ask.com/web?q={search}")
    
    def yandex_search(self, search):
        webbrowser.open_new_tab(f"https://yandex.com/search/?text={search}")

    def ecosia_search(self, search):
        webbrowser.open_new_tab(f"https://www.ecosia.org/search?q={search}")
    
    def facebook_search(self, search):
        webbrowser.open_new_tab(f"https://www.facebook.com/search/top/?q={search}")
    
    def wiki_terminal_search(self, search, lang='en', sentence=1):
        try:
            wikipedia.set_lang(lang)
            print(wikipedia.summary(search, sentences=sentence))
        except Exception as error:
            print(error)
    
    def mail_search(self, search):
        webbrowser.open_new_tab(f"https://mail.google.com/mail/u/0/#search/{search}")

    def palyonyt(self, search):
        pywhatkit.playonyt(search)

