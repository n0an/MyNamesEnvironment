#!/bin/sh
# starwars parser based on eng category page
# For example:
# scrapy crawl starwars_spider -a category="https://starwars.fandom.com/wiki/Category:Males" -o males.csv
scrapy crawl starwars_spider -a category="$1" -o $2
