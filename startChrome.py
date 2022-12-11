from time import sleep
import traceback
import pyautogui as pgui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from startLike import startLike

# Let's noteの画面サイズ：1200*1920

def startChrome(keywords="", username="", password=""):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.instagram.com/")
        
        sleep(1)
        driver.find_elements(By.TAG_NAME, 'input')[0].send_keys(username) #Account name
        driver.find_elements(By.TAG_NAME, 'input')[1].send_keys(password) #Password
        driver.find_elements(By.TAG_NAME, 'button')[1].click() #Login button
        sleep(3)
        
        size = pgui.size()
        driver.set_window_size(size[0] / 3, size[1] * 0.63)
        driver.set_window_position(size[0] / 3, 0)
        
        # 「ログイン情報を保存しますか？」の画面が出たら次へ
        for _ in range(150):
            if driver.find_elements(By.CSS_SELECTOR, '._ab8j'): break
            sleep(0.2)

        while len(keywords):
            keyword = keywords.pop(0)
            sleep(2)
            driver.get("https://www.instagram.com/explore/tags/"+keyword)
            is_except_count_error = startLike(driver=driver, keyword=keyword)
            if is_except_count_error:
                keywords = []
                break

    except Exception:
        traceback.print_exc()
        
    finally:
        try:
            driver.close()
            driver.quit()
        except:
            pass
        
        if keywords:
            sleep(0.1)
            startChrome(keywords=keywords, username=username, password=password)