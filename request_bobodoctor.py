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


def googlemap_mark(bobodoctor_list):
    driver = undetected_chromedriver.Chrome()
    driver.get("https://www.google.com/maps/d/u/0/edit?mid=1kBdz_PMqOs92x4aslfEVPo6iJg3Pihg&ll=24.053457791375514%2C120.104023&z=7")
    driver.maximize_window()
    wait = WebDriverWait(driver, 30)
    try:
        map_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.i4ewOd-r4nke[data-tooltip="未命名的地圖"]')))
        time.sleep(1)
        map_title.click()
        input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Sx9Kwc-i4ewOd-r4nke-fmcmS")))
        input_element.send_keys("波波醫生")
        input_element.send_keys(Keys.ENTER)
    except:
        pass

    for i in range(1,len(bobodoctor_list)):
        print("%s"%bobodoctor_list[i][0]+"%s"%bobodoctor_list[i][1])
        search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tk3N6e-y4JFTd")))
        time.sleep(1)
        # 操作該元素，例如輸入搜尋關鍵字並提交
        search_input.send_keys("%s"%bobodoctor_list[i][0]+"%s"%bobodoctor_list[i][1])
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)
        # 找到 id="addtomap-button" 的元素
        add_to_map_button = wait.until(EC.element_to_be_clickable((By.ID, "addtomap-button")))
        time.sleep(0.5)
        # 使用 JavaScript 點擊
        driver.execute_script("arguments[0].click();", add_to_map_button)
        edit_button = wait.until(EC.element_to_be_clickable((By.ID, "map-infowindow-edit-button")))
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", edit_button)
        editable_div = wait.until(EC.presence_of_element_located((By.ID, "map-infowindow-attr-說明-value")))
        time.sleep(0.5)
        editable_div.send_keys(" " + Keys.SHIFT + Keys.RETURN)
        if bobodoctor_list[i][2] == "":
            bobodoctor_list[i][2] = "未知"
            time.sleep(1)
        editable_div.send_keys("%s %s %s"%(bobodoctor_list[i][2],bobodoctor_list[i][3],bobodoctor_list[i][4]))
        editable_div.send_keys(Keys.RETURN)
    while True:
        time.sleep(1)
googlemap_mark(bobodoctor())
#print(bobodoctor())