import requests
from bs4 import BeautifulSoup
import re

def get_urls_from_archive(domain):
    # Construct the URL for the web.archive.org
    archive_url = f"https://web.archive.org/web/*/{domain}"

    # Fetch the HTML content of the archive page
    response = requests.get(archive_url)
    if response.status_code != 200:
        print("Failed to retrieve data from web.archive.org")
        return []

    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <a> tags with href attribute
    links = soup.find_all('a', href=True)

    # Extract URLs from href attributes using regular expressions
    urls = [link['href'] for link in links if re.match(r'https://web.archive.org/web/\d+/', link['href'])]

    return urls

def main():
    # Take user input for domain name
    domain = input("Enter the domain name: ")

    # Get URLs from web.archive.org
    urls = get_urls_from_archive(domain)

    # Print the retrieved URLs
    print("Retrieved URLs:")
    for url in urls:
        print(url)

if __name__ == "__main__":
    main()
