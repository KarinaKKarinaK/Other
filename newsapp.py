import requests 
import tkinter as tk

def getNews():
    api_key = "5f8025992b704d179dd479b1df0ef59f"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api_key
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])
        
    for i in range(10):
        my_news = my_news + str(i) + ". " + my_articles[i] + "\n"

    label.config(text = my_news)



canvas = tk.Tk()
canvas.geometry("1000x500")
canvas.title("News App")

button = tk.Button(canvas, font=20, text = "Reload", command = getNews, background = "grey")
button.pack(pady = 20)

label = tk.Label(canvas, font = 18, justify = "left")
label.pack(pady = 20)

getNews()

canvas.mainloop()


