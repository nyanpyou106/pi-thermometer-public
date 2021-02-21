import requests
from bs4 import BeautifulSoup

def get_current_geolocation():
    """
    googleで「現在地」と検索した結果の画面から何市にいるかをスクレイピングする
    """
    r = requests.get("https://www.google.co.jp/search?q=%E7%8F%BE%E5%9C%A8%E5%9C%B0")
    soup = BeautifulSoup(r.text, "html.parser")

    city = soup.findAll("div", {"class":"BNeawe deIvCb AP7Wnd"})[0].string

    return city

def scraping_outside_temp():
    """
    googleで「天気」と検索した結果の画面から現在地の外気温をスクレイピングする
    """
    r = requests.get("https://www.google.co.jp/search?q=%E6%B0%97%E6%B8%A9+%E5%A4%A9%E6%B0%97")
    soup = BeautifulSoup(r.text, "html.parser")

    value = soup.findAll("div", {"class":"BNeawe iBp4i AP7Wnd"})[1]
    outside_temperature_value = value.string.split("°")[0]
    return outside_temperature_value

def scraping_currentlocation_outside_temp():
    """
    googleで「現在地＋天気」と検索した結果の画面から現在地の外気温をスクレイピングする
    """
    # 取得できなかったら"nonevalue"の文字列を返す
    r = requests.get("https://www.google.co.jp/search?q=%E7%8F%BE%E5%9C%A8%E5%9C%B0+%E5%A4%A9%E6%B0%97")
    soup = BeautifulSoup(r.text, "html.parser")

    findresult = soup.findAll("div", {"class":"BNeawe iBp4i AP7Wnd"})
    if findresult == []:
        outside_temperature_value = "nonevalue"
    else:
        value = findresult[1]
        outside_temperature_value = value.string.split("°")[0]
    return outside_temperature_value

if __name__ == "__main__":
    #print(get_current_geolocation())
    #print(scraping_outside_temperature())
    print(scraping_currentlocation_outside_temp())