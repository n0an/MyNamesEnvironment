### Scrapy Workflow
*Based on Game of Thrones names parsing*
1. Go to Scrapy/got_stark_names
2. Get url to category of wiki to parse. For example Starks:
```
http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2
```
or all characters:
```
http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%B6%D0%B8
```
3. Run command:
```
./runparse.sh <LINK> <ANY_FILE_NAME>.csv
```
4. Result in the same directory:
 - ANY_FILE_NAME.csv
 - result-excel.xlsx
5. Use result-excel.xlsx file to further steps according to MainWorkflow. You should begin from step [Processing collected data](MainWorkflow.md/#processing-collected-data) of MainWorkflow
