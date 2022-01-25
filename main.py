import time
import requests
from bs4 import BeautifulSoup

query = str(input('Please enter the website for which you wish to know TrustPilot reviews: '))
tp_address = 'https://www.trustpilot.com/review/'
tp_query = tp_address + query.lower()


response = requests.get(tp_query)
soup = BeautifulSoup(response.content,
                     'html.parser')
#function which checks if the query returns a valid(non-404) website on TrustPilot
def queryValidator():
    webpage_status = soup.find('div',
                               class_='errors_error404__tUqzU')
    if webpage_status != None:
        print("Please input a full website domain. (eg. www.google.com or google.com)")
    else:
        tpSearch()

#scraping function which returns the review info
def tpSearch():
    website_rating = soup.find('p',
                               class_='typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3')
    website_rating = website_rating.text
    time.sleep(1)

    website_name = soup.find('span',
                             class_='typography_typography__QgicV typography_h1__Xmcta typography_weight-heavy__E1LTj typography_fontstyle-normal__kHyN3 styles_displayName__GElWn')
    website_name = website_name.text
    time.sleep(1)
    rating_overall_review = soup.find('span',
                                      class_='typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_text__W4hWi')
    overall_review = []
    for item in rating_overall_review:
        overall_review.append(item)
    time.sleep(1)
    review_type = soup.findAll('p',
                               class_='typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_cell__qnPHy styles_labelCell__vLP9S')
    time.sleep(1)
    review_percent = soup.findAll('p',
                                  class_='typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-7__9Ut3K typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_cell__qnPHy styles_percentageCell__cHAnb')
    time.sleep(1)
    for review, percent in zip(review_type, review_percent):
        print(percent.text,'of people reviewed this site as',review.text,'.')
    print('The overall reviews for',website_name,'is',overall_review[-1],
          '({}/5) with a total number of'.format(website_rating), overall_review[0], 'reviews.')



if __name__=='__main__':
    queryValidator()