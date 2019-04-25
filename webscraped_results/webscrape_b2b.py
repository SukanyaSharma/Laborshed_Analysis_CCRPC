from selenium import webdriver
import datetime

CITY = 'Villa_Grove'
DATE = datetime.datetime.today()
browser = webdriver.Firefox()

with open('b2b_{CITY}_{yyyy}-{mm}-{dd}.csv'.format(CITY=CITY, yyyy=DATE.year, mm=DATE.month, dd=DATE.day), 'w') as csvfile:
    for page in range(1, 3):
        url = 'https://www.b2byellowpages.com/bd/illinois/villa-grove-il-business-directory-{}.html'.format(page)
        browser.get(url)
        for elem in browser.find_elements_by_class_name('grouped'):
            text = elem.text.replace('\n', ',')
            print(text)
            csvfile.write(text + '\n')

browser.quit()