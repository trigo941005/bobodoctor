import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver



def bobodoctor():
    return_list = []
    # 網頁的 URL
    url = 'https://popolist999.blogspot.com/2021/06/google.html?m=1'

    # 模擬瀏覽器的 User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }

    # 發送 GET 請求
    response = requests.get(url, headers=headers)

    # 確認請求是否成功
    if response.status_code == 200:
        # 確保使用正確的編碼
        response.encoding = response.apparent_encoding

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到所有 <tr> 標籤並且包含 style="height: 21px;"
        rows = soup.find_all('tr', style="height: 21px;")

        # 檢查是否有找到任何資料
        if rows:

            # 逐一處理每一個 <tr>
            for i, row in enumerate(rows, start=1):
                list1 = []
                # 提取每個 <td> 的文字內容
                cells = row.find_all('td')
                for j, cell in enumerate(cells, start=1):
                    list1.append(f"{cell.text.strip()}")# 列印欄位資料
                return_list.append(list1)
        else:
            print("未找到任何符合的資料。")
    else:
        print(f"無法取得網頁內容，狀態碼：{response.status_code}")
    return return_list


def googlemap_mark():
    driver = undetected_chromedriver.Chrome()
    driver.get("https://www.google.com/maps/d/u/0/edit?mid=1CpzcxlB5GoPW393mzUiKw93xIRuypbw&ll=24.057771183282433%2C120.104023&z=7")
    driver.maximize_window()
    wait = WebDriverWait(driver, 120)

    search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tk3N6e-y4JFTd")))
    time.sleep(1)
    # 操作該元素，例如輸入搜尋關鍵字並提交
    search_input.send_keys("金漾美學診所")
    search_input.send_keys(Keys.ENTER)
    time.sleep(1)
    # 找到 id="addtomap-button" 的元素

    add_to_map_button = wait.until(EC.presence_of_element_located((By.ID, "addtomap-button")))
    
    time.sleep(1)
    # 可以對該元素進行操作，例如點擊
    add_to_map_button.click()
    time.sleep(1)

    edit_button = wait.until(EC.presence_of_element_located((By.ID, "map-infowindow-edit-button")))
        
        # 可以對該元素進行操作，例如點擊
    edit_button.click()
    time.sleep(1)
    editable_div = wait.until(EC.presence_of_element_located((By.ID, "map-infowindow-attr-說明-value")))
    editable_div.send_keys(" " + Keys.SHIFT + Keys.RETURN)
    editable_div.send_keys("111")
    editable_div.send_keys(Keys.RETURN)
    time.sleep(30)

googlemap_mark()
#print(bobodoctor())