import requests
from bs4 import BeautifulSoup

def scrape_news_titles(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        soup= BeautifulSoup(response.text,'html.parser')
        #Find all h2 tags
        h2_tags=soup.find_all('h2')
        title_tag= soup.find('title')
        page_title= title_tag.get_text(strip=True)
        if title_tag:
            []
        else:
            "No page Title Found"

        all_titles=[]
        all_titles.append(f"Page Title: {page_title}")
        all_titles.append("-" * 30)

        # Extract text from <h2> tags
        for h2 in h2_tags:
            title_text=h2.get_text(strip=True)
            if title_text:
                all_titles.append(title_text)

        #save the titles to a text file.
        output_file="news_titles.txt"
        with open(output_file,'w',encoding='utf-8') as file:
            for title in all_titles:
                file.write(title + '\n')
            print(f"Successfully scraped {len(h2_tags) + 1} titles and saved them to '{output_file}'")

    except requests.exceptions. RequestException as e:
        print(f"An error occurred while making the request: {e}")
    except Exception as e:
        print(f"An error occurred : {e}")

news_title_url="https://bbc.com/news"
scrape_news_titles(news_title_url)
