#!/bin/sh
# starwars parser based on eng category page
# For example:
# scrapy crawl gotstarknames -a category="https://starwars.fandom.com/wiki/Category:Males" -o males.csv
scrapy crawl gotstarknames -a category="$1" -o $2
