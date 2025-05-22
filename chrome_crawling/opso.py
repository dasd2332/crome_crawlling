from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from urllib.parse import quote_plus

def search_goole(a):
    baseUrl = 'https://www.google.com/search?sca_esv=6bdcbc1f06d29833&hl=ko&tbm=lcl&sxsrf=ADLYWIJyHYrgzFdPLROWM6KQHi18kzw-6Q:1733643756430&q=맛집+'
    url = baseUrl + quote_plus(a)
    jangso = []
    driver = webdriver.Chrome()
    driver.get(url)
    while True:
        html = driver.page_source
        soup = BeautifulSoup(html, features="lxml")
        r = soup.select('.rllt__details')
        for i in r:
            name = i.select_one('.dbg0pd').text if i.select_one('.dbg0pd') else "No name"
            score = i.select_one('.Y0A0hc').text if i.select_one('.Y0A0hc') else "No score"
            try:
                float(score[0:3])
            except ValueError:
                pass
            else:
                point = float(score[0:3])
            people = score[5:-1]
            place = {"상호명":name, "별점":point, "리뷰 수": people}
            jangso.append(place)

        try:
            more_button = driver.find_element(By.CSS_SELECTOR, '#pnnext')
            more_button.click()
        except Exception as e:
            break
    driver.quit()
    return jangso

