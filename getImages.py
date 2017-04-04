from selenium import webdriver

driver = webdriver.Chrome("C:/chromedriver.exe")

# driver.get('http://lotr.wikia.com/wiki/Aragorn_II_Elessar')
driver.get('http://lotr.wikia.com/wiki/Melkor')


# x = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[3]/div[2]/div[1]/div/a/img")

linksList = driver.find_elements_by_css_selector('.image.image-thumbnail>img')
# x = driver.find_element_by_css_selector('.image.image-thumbnail>img')


selectedLinks = []

if len(linksList) > 1:
    print('More than 1 link found:')
    for link in linksList:
        src = link.get_attribute('src')
        print('Working with link: \n' + src + '\n')
        if (int(link.get_attribute('width')) > 200) and (src.find("wikia.nocookie.net/lotr/images") != -1):
            print('--Size and vignette passed')
            if src.find('.jpg') != -1 or src.find('.png') != 1:
                print('==== extension passed!')
                selectedLinks.append(link)

else:
    print('Only 1 link found:')
    print(linksList[0].get_attribute('src'))

print('Selected links:')

for link in selectedLinks:
    imgSrc = link.get_attribute('src')

    print(imgSrc)

    linkEndPosition = imgSrc.find('/revision')
    cleanedImgSrc = imgSrc[:linkEndPosition]
    print('Link found: ' + cleanedImgSrc)
    driver.get(cleanedImgSrc)
    driver.get_screenshot_as_file('C:/Users/nag/Desktop/aragorn.png')





