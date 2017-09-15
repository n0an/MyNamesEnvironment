#!/bin/sh
# scrapy crawl gotstarknames -a category="http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A2%D0%B0%D1%80%D0%B3%D0%B0%D1%80%D0%B8%D0%B5%D0%BD%D0%BE%D0%B2" -o targarien.csv
scrapy crawl gotstarknames -a category="$1" -o $2
