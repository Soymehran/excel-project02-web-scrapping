from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
service = Service('/mnt/d/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url)
items = driver.find_elements(By.CLASS_NAME, value='ipc-title-link-wrapper')
links = []
for i in items[:250]:
    links.append(i.get_attribute('href'))
    time.sleep(0.05)
urls = links
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

movies_data = []

for url in urls:
    try:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        try:
            title = soup.find('h1').text.strip()
        except:
            title = None
        
        try:
            year = soup.find(string=lambda x: x.strip().isdigit() and len(x.strip()) == 4)
        except:
            year = None
        
        try:
            parental_guide_tags = soup.find_all('a', class_="ipc-link ipc-link--baseAlt ipc-link--inherit-color")
            parental_guide = None
            for tag in parental_guide_tags:
                if "PG-" in tag.text or "R" in tag.text or "G" in tag.text or "NC-17" in tag.text or "Approved" in tag.text:
                    parental_guide = tag.text.strip()
                    break
        except:
            parental_guide = None
        
        try:
            runtime = None
            runtime_ul = soup.find_all('ul', class_='ipc-inline-list ipc-inline-list--show-dividers sc-ec65ba05-2 joVhBE baseAlt')
            if runtime_ul:
                runtime_li = runtime_ul[0].find_all('li')
                for li in runtime_li:
                    if 'h' in li.text and 'm' in li.text:
                        runtime = li.text.strip()
                        break
        except:
            runtime = None
        
        try:
            genres_a = soup.find_all('a', class_="ipc-chip ipc-chip--on-baseAlt")
            genres = [i.text.strip() for i in genres_a]
        except:
            genres = []
        
        try:
            director = soup.find('a', class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text.strip()
        except:
            director = None
        
        try:
            writers_tags = soup.find_all('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
            writer = [writer.get_text(strip=True) for writer in writers_tags[1].find_all('a')] if writers_tags else []
        except:
            writer = []
        
        try:
            star_tags = soup.find_all('ul', class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
            star = [actor.get_text(strip=True) for actor in star_tags[2].find_all('a')] if star_tags else []
        except:
            star = []
        
        try:
            gross_us_canada = None
            for item in soup.find_all('li', role="presentation"):
                if "Gross US & Canada" in item.text:
                    gross_us_canada = item.find('span', class_="ipc-metadata-list-item__list-content-item").text.strip()
                    break
        except:
            gross_us_canada = None
        
        movies_data.append({
            'Title': title,
            'Year': year,
            'Parental Guide': parental_guide,
            'Runtime': runtime,
            'Genres': ', '.join(genres) if genres else None,
            'Director': director,
            'Writer': ', '.join(writer) if writer else None,
            'Star': ', '.join(star) if star else None,
            'Gross US & Canada': gross_us_canada
        })
    except Exception as e:
        print(f"Error processing {url}: {e}")

df = pd.DataFrame(movies_data)
df.to_csv('top_250.csv')