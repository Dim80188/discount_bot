import requests
from bs4 import BeautifulSoup
import json
import time

#
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
}

url = 'https://www.perekrestok.ru/cat/d/'
def get_page(url):
    req = requests.get(url, headers=headers)
    src = req.text
    return src
# #
# def page_write(html):
#     with open('index_k.html', 'w') as file:
#         file.write(html)

# def page_read():
#     with open('index_k.html') as file:
#         src = file.read()
#     return src

# with open('index.html') as file:
#     url_1 = file.read()

def get_categories():
    # soup = BeautifulSoup(page_read(), 'lxml')
    soup = BeautifulSoup(get_page(url), 'lxml')
    all_categories = soup.find_all(class_='cat-list-aside__item')
    categoies_dict = {}
    for cat in all_categories:
        title_cat = cat.find(class_='cat-list-aside__link').text
        link_cat = 'https://www.perekrestok.ru' + cat.find(class_='cat-list-aside__link').get('href')
        categoies_dict[title_cat] = link_cat
    return categoies_dict


# возвращает список категорий
def get_categories_list():
    cat_dict = get_categories()
    categories_list = []
    for k, v in cat_dict.items():
        categories_list.append(k)
    return categories_list

def get_data(url):
    page = get_page(url)
    soup = BeautifulSoup(page, 'lxml')
    # soup = BeautifulSoup(page_read(), 'lxml')
    all_products_card = soup.find_all(class_='sc-dlfnbm ldVxnE')
    all_products_page = []
    for card in all_products_card:
        title = card.find(class_='product-card__title').text
        price_new = card.find(class_='price-new').text
        # price_old = card.find(class_='price-old').text
        discont = card.find(class_='product-card__badge').span.text
        link = 'https://www.perekrestok.ru' + card.find(class_='product-card__link').get('href')
        all_products_page.append(
            {
                "Title": title,
                "Price_new": price_new,
                "Discont": discont,
                "Link": link
            }
        )
    return all_products_page

def get_pagination(url):
    page = get_page(url)
    soup = BeautifulSoup(page, 'lxml')
    # soup = BeautifulSoup(url_1, 'lxml')
    pagination_block = soup.find(class_='rc-pagination pagination')
    if pagination_block:
        pagination_block = pagination_block.find_all('li')
        pag_end = pagination_block[-3].get('title')
        return pag_end

#подставляю url категории и получаю список продуктов
def get_product_categories(url):
    all_page = []
    if get_pagination(url):
        str = int(get_pagination(url))
        # all_page = []
        for i in range(1, (str+1)):

            link_pag = url + f'?page={i}'

            data_page = get_data(link_pag)
            all_page.extend(data_page)
        return all_page
            # save_file(link, all_page)
                    # time.sleep(3)
    else:
        all_page = get_data(url)
        # save_file(link, data_page)
                # time.slip(3)
        return all_page



def save_file(url, all_data):
    soup = BeautifulSoup(get_page(url), 'lxml')
    # soup = BeautifulSoup(page_read(), 'lxml')
    name = soup.find(class_='page-header__title').text
    name = name.split(':')[0]
    name = name.replace('/', '-')
    with open(f'data/{name}.json', 'a', encoding='utf-8') as file:
        json.dump(all_data, file, indent=4, ensure_ascii=False)



if __name__ == "__main__":
    print(get_categories())
    # url = 'https://www.perekrestok.ru/cat/d/'
    # cat_list = get_categories()
    #
    # for link in cat_list:
    #     if get_pagination(link):
    #         str = int(get_pagination(link))
    #         all_page = []
    #         for i in range(1, (str+1)):
    #
    #             link_pag = link + f'?page={i}'
    #
    #             data_page = get_data(link_pag)
    #             all_page.extend(data_page)
    #         save_file(link, all_page)
    #             # time.sleep(3)
    #     else:
    #         data_page = get_data(link)
    #         save_file(link, data_page)
    #         # time.slip(3)
