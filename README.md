# Task-3
Using BeautifulSoup for web scraping, for parsing HTML tags like &lt;h2> and &lt;title>. Saving the extracted data to a text file.

Specify the URL: Define the URL of the news website you want to scrape.

Send an HTTP Request: Use requests.get() to fetch the HTML content from the URL. Check if the request was successful by verifying the status code (a 200 status code means "OK").

Parse the HTML: Create a BeautifulSoup object by passing the HTML content and the parser you want to use (usually 'html.parser').
Find the Tags: Use BeautifulSoup's methods like find_all() to locate all the <h2> and <title> tags on the page.

Extract the Text: Loop through the found tags and extract the text content from each. The .text attribute is perfect for this.
Save to a Text File: Open a file in write mode ('w'), loop through your list of titles, and write each title to a new line in the file.
