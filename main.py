

# import pdb
#
# url = 'http://www.nettruyen.com/truyen-tranh/toi-cuong-phan-sao-lo-he-thong/chap-233/581775'
#
#
# def get_page_content(url):
#     page = requests.get(url, headers={"Accept-Language": "en-US"})
#     return bs4.BeautifulSoup(page.text, "html.parser")
#
#
# soup = get_page_content(url)
#
# page_chapper = soup.findAll('div', class_='page-chapter')
# for page in page_chapper:
#     image = page.find('img')['data-original']
#     name = page.find('img')['alt']
#     page_number = page.find('img')['data-index']
#
#     print(name, page_number, image)