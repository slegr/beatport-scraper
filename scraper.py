import requests
from bs4 import BeautifulSoup

# CONSTANTS TO MODIFY
file_name = "DnB_to_download.txt"
url_list = [
    "https://www.beatport.com/genre/drum-bass/1/top-100",
    "https://www.beatport.com/genre/drum-bass/1/top-100-releases",
]
# URL Examples
# https://www.beatport.com/genre/drum-bass/1/top-100
# https://www.beatport.com/genre/drum-bass/1/top-100-releases
# https://www.beatport.com/genre/drum-bass/1/tracks?subgenre=5
# https://www.beatport.com/genre/dubstep/1/top-100





# DO NOT MODIFY THE CODE BELOW
tracks = []
for url in url_list:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("li", {"data-ec-type": "product"})

    print("Found {} tracks on {}".format(len(results), url))

    for result in results:
        titles = result.find("p", {"class": "buk-track-title"})
        if titles is None:
            titles = result.find("p", {"class": "buk-horz-release-title"}).find_all("a")
        else:
            titles = titles.find_all("span")
        
        artists = result.find("p", {"class": "buk-track-artists"})
        if artists is None:
            artists = result.find("p", {"class": "buk-horz-release-artists"}).find_all("a")
        else:
            artists = artists.find_all("a")
        
        title = titles[0].text
        remix = f"({titles[1].text})" if len(titles) > 1 else ""
        artists = [a.text for a in artists][:4]
        artists = ", ".join(artists)
        tracks.append("{} - {} {}".format(artists, title, remix))

print("Found {} tracks".format(len(tracks)))
tracks_set = set(tracks)
print("Found {} unique tracks".format(len(tracks_set)))
tracks_set = sorted(tracks_set)
with open(file_name, "w", encoding="utf-8") as f:
    for track in tracks_set:
        f.write(track + "\n") 