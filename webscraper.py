from bs4 import BeautifulSoup
import requests
import os


def scrape_website(url, tagsearch=None, class_name=None, id_name=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        soup = BeautifulSoup(response.content, 'lxml')

        # Display the title of the webpage
        page_title = soup.title.string if soup.title else 'No title found'
        print(f"Page Title: {page_title}\n")

        # If tagsearch is provided, search for tag, class, or id
        if tagsearch:
            if class_name:
                tags = soup.find_all(tagsearch, class_=class_name)
            elif id_name:
                tags = [soup.find(tagsearch, id=id_name)]
            else:
                tags = soup.find_all(tagsearch)
        else:
            # Default to searching for title if no tag is provided
            tags = soup.find_all('title')

        # Print the found tags
        if tags:
            for tag in tags:
                print(tag.prettify())  # Pretty-print HTML elements
                print("\n" + "-" * 80 + "\n")
        else:
            print(f"No tags found for the search criteria.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error occurred: {req_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def save_to_file(content, filename="scraped_content.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Scraped content saved to {os.path.abspath(filename)}")


if __name__ == "__main__":
    url = input('Enter URL: ')
    tagsearch = input('Enter a tag to search (optional): ')
    class_name = input('Enter a class name (optional): ')
    id_name = input('Enter an id name (optional): ')

    # Scrape the website
    scrape_website(url, tagsearch, class_name, id_name)
