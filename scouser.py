import scrapy

class LiverpoolSpider(scrapy.Spider):
    name = 'scouser'
    start_urls = ['https://www.premierleague.com/clubs/10/Liverpool/squad']

    def parse(self, response, **kwargs):
        for player_card in response.css('li.stats-card'):
            yield {
                'name': player_card.css('div.stats-card__player-first::text').get(),
                'surname': player_card.css('div.stats-card__player-last::text').get(),
                'position': player_card.css('div.stats-card__player-position::text').get(),
                'country': player_card.css('span.stats-card__player-country::text').get()
            }