import webbrowser
import wikipedia
import requests

def yt_search(search: str):
    webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={search}")

def google_search(search: str):
    webbrowser.open_new_tab(f"https://www.google.com/search?q={search}")

def bing_search(search: str):
    webbrowser.open_new_tab(f"https://www.bing.com/search?q={search}")

def duck_search(search: str):
    webbrowser.open_new_tab(f"https://duckduckgo.com/?q={search}")

def yahoo_search(search: str):
    webbrowser.open_new_tab(f"https://search.yahoo.com/search?p={search}")

def ask_search(search: str):
    webbrowser.open_new_tab(f"https://www.ask.com/web?q={search}")

def yandex_search(search: str):
    webbrowser.open_new_tab(f"https://yandex.com/search/?text={search}")

def ecosia_search(search: str):
    webbrowser.open_new_tab(f"https://www.ecosia.org/search?q={search}")

def fb_search(search: str):
    webbrowser.open_new_tab(f"https://www.facebook.com/search/top/?q={search}")

def wiki_terminal_search(search: str, lang='en', sentence=1):
    try:
        wikipedia.set_lang(lang)
        print(wikipedia.summary(search, sentences=sentence))
    except Exception as error:
        print(error)
        return error
    
def mail_search(search: str):
    webbrowser.open_new_tab(f"https://mail.google.com/mail/u/0/#search/{search}")

def wiki_web_search(search: str):
    webbrowser.open_new_tab(f"https://en.wikipedia.org/wiki/{search}")

def test_site(search: str):
    """please enter site name with http information"""
    try:
        r = requests.get(search)

    except Exception as error:
        print(error)
        return "site not working"
    
    if r.status_code == 200:
        print("site working")
        return "site working"
