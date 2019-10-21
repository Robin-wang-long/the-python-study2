import requests
from bs4 import BeautifulSoup
import csv


def get__information(city__pinyin):
    url = 'http://pm25.in/' + city__pinyin
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    div_list = soup.find_all('div', {'class': 'span1'})
    city_aqi = []
    for i in range(8):
        div_caption = div_list[i]
        caption = div_caption.find('div', {'class': 'caption'}).text.strip()
        value = div_caption.find('div', {'class': 'value'}).text.strip()
        city_aqi.append( value)
    return city_aqi


def get_allcity():
    url = 'http://pm25.in/'
    city__list = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    city__div = soup.find_all('div', {'class': 'bottom'})[1]
    city__list__link = city__div.find_all('a')
    for city in city__list__link:
        city__name = city.text
        city__pinyin = city['href'][1:]
        city__list.append((city__name, city__pinyin))
    return city__list


def main():
    city__list = get_allcity()

    header = ['City', 'AQI', 'pm2.5/1h', 'pm10/1h', 'co/1h', 'co2/1h', 'o3/1h', 'o3/8h', 'so2/1h']

    with open('city__information.csv', 'w', encoding='UTF-8', newline='')as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for i, city in enumerate(city__list):
            if (i+1) % 10 == 0:
                print('已处理第{}，共{}条数据'.format(i+1, len(city__list)))
            city__name = city[0]
            city__pinyin = city[1]
            city__get = get__information(city__pinyin)
            row = [city__name] + city__get
            writer.writerow(row)


if __name__ == '__main__':
    main()