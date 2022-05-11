from time import sleep
import traceback
import pyautogui as pgui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from likeLike import likeLike

# Let's noteの画面サイズ：1200*1920

def likeChrome(keywords="", user_name="handaicompa", password="wpyrki"):
    try:
        # print(pgui.displayMousePosition())

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.instagram.com/")

        sleep(1)
        driver.find_elements_by_tag_name('input')[0].send_keys(user_name) #id
        driver.find_elements_by_tag_name('input')[1].send_keys(password) #password
        driver.find_elements_by_tag_name('button')[1].click() #login
        
        size = pgui.size()
        print(size)
        driver.set_window_size(size[0] / 3, size[1] * 0.6)
        driver.set_window_position(size[0] / 3, 0)

        for _ in range(150):
            try:
                driver.find_element_by_css_selector('._6q-tv')
                break
            except:
                sleep(0.2)
                pass

        try:
            driver.find_element_by_css_selector('.HoLwm').click()
        except:
            pass

        if keywords==[]:
            driver.find_elements_by_tag_name('input')[0].send_keys("#")
            likeLike(driver=driver)

        while keywords!=[]:
            keyword = keywords.pop(0)
            driver.get("https://www.instagram.com/explore/tags/"+keyword)
            is_except_count_error = likeLike(driver=driver, keyword=keyword)
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
        
        if keywords != []:
            likeChrome(keywords=keywords, user_name=user_name, password=password)
