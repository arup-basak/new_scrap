import urllib.parse as urlparse
import requests
from bs4 import BeautifulSoup


def search(keyword):
    url = 'https://google.com/search?' + urlparse.urlencode({'q': keyword})
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all(class_="g"))

search("Kolkata Riots")


# Find all the search results with class="g"
# results = soup.find_all(class_="g")
#
# # Loop through the results and print the title and summary of each result
# for result in results:
#     # Find the title element
#     title = result.find("h3")
#     # Find the summary element
#     summary = result.find(class_="st")
#     # Check if both elements exist
#     if title and summary:
#         # Print the title and summary
#         print(title.text)
#         print(summary.text)
#         print("-----")
#
#
# if soup:
#     # Extract desired information from the results page using Beautiful Soup
#     results = soup.find_all("h3", class_="r")  # Find search result titles (adapt selector as needed)
#
#     for result in results:
#         link = result.find("a")["href"]
#         title = result.text
#         print(f"Title: {title}\nLink: {link}\n")
