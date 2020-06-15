import pdb
import urllib
from time import sleep

from selenium import webdriver
import bs4
import pandas
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def get_page_content(url):
    page = requests.get(url, headers={"Accept-Language": "en-US"})
    text = page.text
    page.connection.close()
    return bs4.BeautifulSoup(text, "html.parser")


def closeRequestAdapter():
    # s = requests.session()
    # s.config['keep_alive'] = False
    print('a')


def getListHrefChapOfCommic(url_commic):
    browser = webdriver.Chrome(executable_path=r"E:\chromedriver_win32\chromedriver.exe")
    browser.get(url_commic)

    list_chap_elem = browser.find_element_by_class_name('list-chapter')  # Find the search box

    row_list = list_chap_elem.find_elements_by_class_name('row')

    list_href_of_commic = []

    index = 0
    for item in reversed(row_list):
        if index != (len(row_list) - 1):
            a_tag = item.find_element_by_tag_name('a')
            href = a_tag.get_attribute('href')
            list_href_of_commic.append(href)

        index += 1

    browser.quit()

    return list_href_of_commic


# def downloadIamge():

def saveImage(name, url):
    with open(name + '.jpg', 'wb') as handle:
        response = requests.get(url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)


def crawImageOfChap(href_chap):
    print('---------------------------------------------------------------------------------')
    print('NEW CHAPTER')
    print(href_chap)
    soup = get_page_content(href_chap)

    page_chapper = soup.findAll('div', class_='page-chapter')
    for page in page_chapper:
        image = page.find('img')['src']
        name = page.find('img')['alt']
        page_number = page.find('img')['data-index']

        saveImage(name, image)
        print(name, page_number, image)


def crawImageWithSelenium(href_chap):
    browser = webdriver.Chrome(executable_path=r"E:\chromedriver_win32\chromedriver.exe")
    browser.get(href_chap)

    list_image_elm = browser.find_elements_by_class_name('page-chapter')

    # for img in list_image_elm:
    img_tag = list_image_elm[0].find_element_by_tag_name('img')
    href = img_tag.get_attribute('src')

    browser.get(href)

    # browser.save_screenshot("screenshot.png")

    # browser.back()

    # script_js = 'var link = document.createElement("a"); link.download = true; link.href = "' + str(
    #     href) + '"; document.body.appendChild(link); link.click(); document.body.removeChild(link); delete link;'
    #
    # # pdb.set_trace()
    #
    # browser.execute_script(script_js)


def main():
    list_href_chap_commic = getListHrefChapOfCommic(
        'http://www.nettruyen.com/truyen-tranh/toi-cuong-phan-sao-lo-he-thong/')

    # for href_chap in list_href_chap_commic:
    # crawImageOfChap(href_chap)

    crawImageWithSelenium(list_href_chap_commic[0])

    # sleep(10)
