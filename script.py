import requests
import re
from bs4 import BeautifulSoup
from datetime import date

url = "https://bamboohousing.ca/homepage?StartTerm=Fall&RoomsAvailable=3&Coed=&UwaterlooDist=&LeaseType=4%20Month%20Sublet&Price=&Sort=Recent"

response = requests.get(url)

print("Listings for ", date.today().strftime("%B %d, %Y"))
print('')

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    no_listings_found = soup.find_all("h3", class_="header")
    if no_listings_found:
        print("No listings today :(")
    else:
        listings = soup.find_all("div", class_="item")
        for listing in listings:
            title = listing.find("p")
            if title:
                if re.search("25.* Phillip St", title.text):
                    print("(REZONE ALERT)", end='')
                print(title.text)
else:
    print("Failed to retrieve data from the URL.")

print('')