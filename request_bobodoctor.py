import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import undetected_chromedriver
import data

def replace_non_bmp(text, replacement='?'):
    return ''.join(c if ord(c) <= 0xFFFF else replacement for c in text)


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
    print(return_list)
    return return_list


def googlemap_mark(bobodoctor_list):
    url = data.data()[2]
    driver = undetected_chromedriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    # 使用 id 定位

    email_input = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
    # 輸入電子郵件地址
    email_input.send_keys(data.data()[0])
    email_input.send_keys(Keys.ENTER)
    # 使用 id 定位（假設你可以找到 id，這裡用 name 作為示例）
    time.sleep(5)
    password_input = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
    # 輸入密碼
    password_input.send_keys(data.data()[1])
    password_input.send_keys(Keys.ENTER)
    try:
        map_title = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.i4ewOd-r4nke[data-tooltip="未命名的地圖"]')))
        time.sleep(1)
        map_title.click()
        input_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "Sx9Kwc-i4ewOd-r4nke-fmcmS")))
        input_element.send_keys("波波醫生")
        input_element.send_keys(Keys.ENTER)
    except:
        pass
        
    for i in range(1, len(bobodoctor_list)):
        # 替換處理
        bobodoctor_list[i] = [replace_non_bmp(item) for item in bobodoctor_list[i]]

        retry_count = 0  # 初始化重試計數
        while True:  # 開始重試迴圈
            try:
                if bobodoctor_list[i][1] == "":
                    break
                if "學" in bobodoctor_list[i][1] and "醫" not in bobodoctor_list[i][1] and "診所" not in bobodoctor_list[i][1]:
                    break
                print(f"處理第 {i} 個標記: {bobodoctor_list[i]}")
                search_input = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tk3N6e-y4JFTd")))
                time.sleep(3)

                # 操作搜尋框並提交
                search_input.send_keys(f"{bobodoctor_list[i][0]} {bobodoctor_list[i][1]}")
                search_input.send_keys(Keys.ENTER)
                time.sleep(1)

                # 嘗試找到並點擊 "加入地圖" 按鈕
                try:
                    add_to_map_button = wait.until(EC.element_to_be_clickable((By.ID, "addtomap-button")))
                except Exception as e:
                    print(f"未找到 '加入地圖' 按鈕 (標記 {i})，重試中...")
                    retry_count += 1
                    if retry_count > 5:  # 超過5次重試就跳過該標記
                        print(f"第 {i} 個標記失敗，已跳過。")
                        break
                    continue  # 重新嘗試本次迭代
                
                # 點擊 "加入地圖" 按鈕
                driver.execute_script("arguments[0].click();", add_to_map_button)

                # 點擊 "編輯" 按鈕
                edit_button = wait.until(EC.element_to_be_clickable((By.ID, "map-infowindow-edit-button")))
                zzz()  # 自定義延遲函數
                driver.execute_script("arguments[0].click();", edit_button)

                # 找到說明欄並添加內容
                editable_div = wait.until(EC.presence_of_element_located((By.ID, "map-infowindow-attr-說明-value")))
                zzz()
                editable_div.send_keys(" " + Keys.SHIFT + Keys.RETURN)

                # 確保有描述內容，否則填入 "未知"
                if not bobodoctor_list[i][2]:
                    bobodoctor_list[i][2] = "未知"
                    zzz()

                editable_div.send_keys(f"{bobodoctor_list[i][2]} {bobodoctor_list[i][3]} {bobodoctor_list[i][4]}")
                editable_div.send_keys(Keys.RETURN)

                print(f"第 {i} 個標記成功完成！")
                break  # 跳出重試迴圈，進行下一個標記

            except Exception as e:
                retry_count += 1
                print(f"第 {i} 個標記處理出錯: {e}，重試中 (第 {retry_count} 次)...")
                if retry_count > 5:  # 超過5次重試就跳過該標記
                    print(f"第 {i} 個標記失敗，已跳過。")
                    while True:
                        time.sleep(1)
                time.sleep(3)  # 延遲後重新嘗試
    while True:
        time.sleep(1)
def zzz():
    time.sleep(1)
googlemap_mark(bobodoctor())