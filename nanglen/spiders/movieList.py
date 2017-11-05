# -*- coding: utf-8 -*-
import scrapy
import datetime
from nanglen.items import MovieItem

class MovieSpider(scrapy.Spider):
    name = 'movieList'
    allowed_domains = ['majorcineplex.com']
    start_urls = ['http://www.majorcineplex.com/movie']

    # def parse(self, response):
    #     pass


    # def start_requests(self):
    #     url = "http://www.majorcineplex.c
    #     yield scrapy.FormRequest(url, callback=self.parse, method="GET")

    def parse(self, response):
        movies = response.css("div.allMovies")
        movie_list = movies.css("div.eachMovie")
        # movieList.extend(movies.css("div.eachMoviepl"))
        for movie in movie_list:
            movie_link = movie.css("a.btn-nameMovie::attr(href)").extract()[0]
            movie_link = movie_link.split('/')
            movie_link.insert(3, "en")
            movie_link_en = '/'.join(movie_link)
            request = scrapy.Request(movie_link_en, callback=self.scrap_movie)
            yield request


    
    @classmethod
    def scrap_movie(self, response):
        def remove_white_space(text):
            return text.strip()
        item = MovieItem()
        item['Title'] = response.css('meta[property="og:title"]::attr(content)').extract()[0].strip()
        item['Genre'] = response.css('div.descmoviegenre').css('span::text').extract()
        time = response.css('div.descmovielength').css('span::text').extract()
        seperate_time = time[1].split(' ')
        minute = time[0].split(' ')
        item['Year'] = seperate_time[2]
        item['ReleaseDate'] = time[1]
        item['Length'] = minute[0]
        item['Synopsis'] = response.css('meta[property="og:description"]::attr(content)').extract()[0]
        item['PosterUrl'] = response.css('div.posterMovie').css('img::attr(src)').extract()[0]
        item['Director'] = response.css('.txt-dteam::text').extract()[0].strip()
        actors = response.css('#_actor1').css('span::text').extract()[1].strip().split(',')
        actors = [remove_white_space(actor) for actor in actors]
        item['Actors'] = actors
        return item

    # Title = Field()
    # ReleaseDate = Field()
    # Length = Field()
    # Genre = Field()
    # Synopsis = Field()