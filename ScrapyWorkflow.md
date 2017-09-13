### Scrapy workflow

1. Get Rus Urls:

Open scrapy shell:
```
scrapy shell
fetch("http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2")
```
Copy paste this script:
```
def get_urls(response):

    table = response.xpath('//*[@class="mw-content-ltr"]')[1]

    links = table.xpath('.//a/@href').extract()

    urls = []

    for link in links:
        url = 'http://ru.gameofthrones.wikia.com' + link
        urls.append(url)
        print('url = ',url)
        #yield {'Url': url}
    return urls
```
Run this command:
```
urls = get_urls(response)
urls
```
You have list of names rus urls now.

2. Get Rus Names
Use scrapy spider: **got_stark_names**
```
scrapy crawl gotstarknames -o rusitems.json
```

3. Get Eng Urls
**Get Eng Urls from collected Rus json file:**

Open python and copy paste script:
```
import json
with open('rusitems.json') as data_file:
  data = json.load(data_file)

engurls = []
for index in range(0, len(data)):
  engurls.append(data[index]["Eng Url"])

flat_urls = [item for sublist in engurls for item in sublist]
```
**Next use flat_urls as starting urls list in Eng Names parser**

4. Get Eng Names
Use scrapy spider: **got_stark_names_eng**
```
scrapy crawl gotspider -o engitems.json
```
