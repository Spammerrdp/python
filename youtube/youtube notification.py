import requests
import pytube
l1 = ("\nfit tuber hindi\nfit tuber\nBageshwar Dham Sarkar\nPRJ motive\nCodeWithHarry \nMurtaza's Workshop - Robotics and AI\nKishan Chotaliya\nYouth Philosophy")
with open("youtube.txt", "r")as kl:
    ll = kl.read()
    ll=ll.split("\n")
try:
    u = int(input(
        "select youtuber -\nfit tuber hindi\nfit tuber\nBageshwar Dham Sarkar\nPRJ motive\nCodeWithHarry \nMurtaza's Workshop - Robotics and AI\nKishan Chotaliya\nYouth Philosophy\nCustom\nEnter Here:"))
    if u == 8:
        topic = input("enter topic")
    else:
        topic = ll[u]

except  Exception as e:
    topic = ll[2]
def playonyt(topic: str, use_api: bool = False):
    if use_api:
        response = requests.get(
            f"https://pywhatkit.herokuapp.com/playonyt?topic={topic}"
        )
    else:
        url = f"https://www.youtube.com/results?q={topic}"
        count = 0
        cont = requests.get(url)
        data = cont.content
        data = str(data)
        lst = data.split('"')
        for i in lst:
            count += 1
            if i == "WEB_PAGE_TYPE_WATCH":
                break
        vurl = f"https://www.youtube.com{lst[count - 5]}"
        yt = pytube.YouTube(vurl)
        video = yt.streams.get_highest_resolution()
        video.download()
        print(video.title)


playonyt(topic)

