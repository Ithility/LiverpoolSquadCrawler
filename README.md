# LiverpoolSquadCrawler

1. Ensure you have Python installed on your system. You can download it from python.org.
2. Install Scrapy. You can install Scrapy using pip, Python's package manager, by running the following command:

         pip install scrapy

4. Clone or download this repository to your local machine.
5. Navigate to the directory where you have cloned or downloaded this repository.
6. Run the spider using the following command: 
       
        scrapy crawl scouser -o output_file.json


Spider Explanation
Name: LiverpoolSpiderThis is the main class representing the Scrapy spider. It inherits from Scrapy's Spider class.
Start URLs:The spider starts crawling from the URL specified in the start_urls attribute. In this case, it starts from the Liverpool squad page on the Premier League website.
parse Method:This method is called to handle the response from the start URLs or any subsequent URLs encountered during crawling. It extracts information about each player from the HTML response using CSS selectors and yields a dictionary containing the player's name, surname, position, and country.
response.css('li.stats-card'): Selects each player card element on the page.
player_card.css('div.stats-card__player-first::text').get(): Extracts the first name of the player.
player_card.css('div.stats-card__player-last::text').get(): Extracts the last name of the player.
player_card.css('div.stats-card__player-position::text').get(): Extracts the position of the player.
player_card.css('span.stats-card__player-country::text').get(): Extracts the country of the player.
