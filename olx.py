import requests
from bs4 import BeautifulSoup


    # план действий:
    #   1 выясняем количество страниц
    #    2 формируем список ссылок на страницы выдачи
    #     3 собрать данные



def get_html(url):
    r = requests.get(url)
    return r.text # получаем текстовый вид html указанного адреса

def get_total_pages (html):   #выясняем количество страниц
   soup = BeautifulSoup(html , 'lxml')
   pages = soup.find ('div' , class_= "pager rel clr").find_all('span', class_ = "item fleft")[-1].find('a').get("href")
   #ищет все элементы с джанным класом, выбирает последний элемент и находит номер последней страницы
   total_pages = pages.split('=')[1]
   return int(total_pages) # возвращаем общее количество страниц



def main():   # формируем список ссылок на страницы выдачи
    url = "https://www.olx.ua/zhivotnye/sobaki/krivoyrog/"
    base_url = "https://www.olx.ua/zhivotnye/sobaki/krivoyrog/"
    query_part = "q- /"
    page_part = "?page="

    total_pages = get_total_pages(get_html(url))

    for i in range(1, total_pages):
        url_gen = base_url + page_part + str(i) # + query_part
        print(url_gen)



# видео парсинг avito.ru 0:20:00

#для CMD:

# import requests
# url = str ("https://www.olx.ua/dom-i-sad/instrumenty/krivoyrog/")


# r = requests.get(url)
# r.text
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'lxml')
#pages = soup.find ('div' , class_= "pager rel clr").find_all('span', class_ = "item fleft")[-1].find('a').get("href")
#total_pages = pages.split('=')[1]
#print(total_pages)





if __name__ == '__main__':
    main()