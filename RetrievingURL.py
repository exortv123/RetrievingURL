import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
count = input("Enter count: ")
position = input("Position: ")
val1 = 0
val2 = 0

print("Retrieving:", url)
while val1 < int(count):
    html = urllib.request.urlopen(url).read()
    parser = BeautifulSoup(html, "html.parser")
    aTag = parser("a")
    for tag in aTag:
        val2 += 1
        if not val2 == int(position): continue
        link = tag.get("href", None)
        print("Retrieving:", link)
        url = link
    val2 = 0
    val1 += 1