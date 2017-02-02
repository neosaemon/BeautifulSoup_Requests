import requests
from bs4 import BeautifulSoup
import csv


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


def write_csv(title):
    with open('olx_pets.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(title)



def get_page_data(html):
    # print(html)
    soup = BeautifulSoup(html , 'lxml')

    adverts_all = soup.find ('div', class_="content").find('div',class_="rel listHandler ").find('table', class_ = "fixed offers breakword ").find_all('td', class_="offer ")

    # print(str(adverts_all))

    for adwert in adverts_all:
             #title, price
        try:
            # title = adwert.find('td', class_="offer ").find_all('href').text
            title = {adwert.find('h3').text.strip()}
        except:
            title = "-------"


        print(title)
        write_csv(title)

def main():   # формируем список ссылок на страницы выдачи
    url = "https://www.olx.ua/hobbi-otdyh-i-sport/sport-otdyh/krivoyrog/"
    base_url = "https://www.olx.ua/hobbi-otdyh-i-sport/sport-otdyh/krivoyrog/"
    query_part = "q-ролики/"
    page_part = "?page="

    total_pages = get_total_pages(get_html(url))
    # print(total_pages)

    for i in range(2,total_pages):
        url_gen = base_url + query_part + page_part + str(i)  # + query_part
        print(url_gen)
        html = get_html(url_gen)
        get_page_data(html)



# видео парсинг avito.ru 0:20:00

#для CMD:

# import requests
# url = str ("https://www.olx.ua/zhivotnye/sobaki/krivoyrog/")


# r = requests.get(url)
# r.text
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(r.text, 'lxml')
#pages = soup.find ('div' , class_= "pager rel clr").find_all('span', class_ = "item fleft")[-1].find('a').get("href")
#total_pages = pages.split('=')[1]
#print(total_pages)





if __name__ == '__main__':
    main()