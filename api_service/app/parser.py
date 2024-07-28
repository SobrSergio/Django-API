from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from .models import Ad
import time

def fetch_ads():
    # Настройки для Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-gpu")
    chrome_service = Service('/usr/local/bin/chromedriver') 
    

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    base_url = "https://www.farpost.ru"
    driver.get(base_url + "/vladivostok/service/construction/guard/+/Системы+видеонаблюдения/")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'table.viewdirBulletinTable'))
    )
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    table = soup.find('table', class_='viewdirBulletinTable')
    if not table:
        driver.quit()
        raise ValueError("Не удалось найти таблицу с объявлениями")

    tbody = table.find('tbody', class_='native')
    if not tbody:
        driver.quit()
        raise ValueError("Не удалось найти tbody с объявлениями")
    
    ads = []
    for i, row in enumerate(tbody.find_all('tr', class_='bull-list-item-js -exact'), start=1):
        ad_id = row.get('data-doc-id')
        if not ad_id:
            continue

        title_tag = row.find('a', class_='bulletinLink')
        title = title_tag.text.strip() if title_tag else "Нет заголовка"

        views_tag = row.find('span', class_='views')
        views = int(views_tag.text.strip()) if views_tag else 0

        ad_url = base_url + title_tag['href']
        driver.get(ad_url)
        time.sleep(2)
        
        ad_soup = BeautifulSoup(driver.page_source, 'html.parser')
        seller_summary = ad_soup.find('div', class_='seller-summary-user')
        author_tag = seller_summary.find('a') if seller_summary else None
        author = author_tag.text.strip() if author_tag else "Неизвестен"

        position = i

        ads.append({
            'title': title,
            'ad_id': int(ad_id),
            'author': author,
            'views': views,
            'position': position,
        })

        if i == 10:
            break

    driver.quit()
    return ads

def save_ads_to_db():
    ads = fetch_ads()
    for ad_data in ads:
        Ad.objects.update_or_create(
            ad_id=ad_data['ad_id'],
            defaults=ad_data
        )
