# # -*- coding: utf-8 -*-

# # Define here the models for your scraped items
# #
# # See documentation in:
# # http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

# class NanglenItem(Item):
#     # define the fields for your item here like:
#     # name = Field()
#     pass

class MovieItem(Item):
    Title = Field()
    ReleaseDate = Field()
    Year = Field()
    Length = Field()
    Genre = Field()
    Synopsis = Field()
    PosterUrl = Field()
    LastOnAir = Field()
    Actors = Field()
    Director = Field()
