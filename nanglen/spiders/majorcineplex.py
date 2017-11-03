# import scrapy

# class MajorSpider(scrapy.Spider):
#     name = 'movies'

#     # allowed_domains = ['example.com']
#     # start_urls = ['http://example.com/']


#     def start_requests(self):   
#         url = "http://www.majorcineplex.com/ajaxbooking/ajax_showtime"
#         frmdata = {
#             "cinema_text": "13",
#             "date_link": "2017-10-25"
#         }
#         yield scrapy.FormRequest(url, callback=self.parse, formdata=frmdata, method="POST")

#     def parse(self, response):
#         # self.logger.info('A response from %s just arrived!')
#         for theatre in response.css("div.book_st_row"):
#             theatreObj = {
#                 "theaterName" : theatre.css('div.book_st_theatre').extract(),
#                 "movieArray": []
#             }
#             for movie in theatre.css('div.book_st_right_box'):
#                 # theatreObj.movieArray
#                 movieObj = {
#                     "movieName" :  movie.css('div.book_st_mvname').extract(),
#                     "movieShowtimes" : []
#                 }
#                 for showtime in movie.css('div.book_st_inside'):
#                     movieObj["ageRating"] = 
#                     movieObj.movieShowtimes.append({

#                     })

