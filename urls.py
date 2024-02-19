import re

import requests
from bs4 import BeautifulSoup


def get_urls_from_archive(domain):
    # Construct the URL for the web.archive.org
    archive_url = f"https://web.archive.org/web/*/{domain}"

    # Fetch the HTML content of the archive page
    response = requests.get(archive_url)
    if response.status_code != 200:
        print("Failed to retrieve data from web.archive.org")
        return []

    # Parse HTML content
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all <a> tags with href attribute
    links = soup.find_all("a", href=True)

    # Extract URLs from href attributes using regular expressions
    urls = [
        link["href"]
        for link in links
        if re.match(r"https://web.archive.org/web/\d+/", link["href"])
    ]

    return urls


def save_urls_to_file(urls, file_path):
    with open(file_path, "w") as f:
        for url in urls:
            f.write(url + "\n")


def main():
    # Take user input for domain name
    domain = input("Enter the domain name: ")

    # Get URLs from web.archive.org
    urls = get_urls_from_archive(domain)

    # Ask user for the path to save the output text file
    file_path = input("Enter the path to save the output text file: ")

    # Save URLs to the output text file
    save_urls_to_file(urls, file_path)
    print("URLs saved to", file_path)


if __name__ == "__main__":
    main()
