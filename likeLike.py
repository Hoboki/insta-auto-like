import datetime
from time import sleep
import traceback
from random import uniform
import pyautogui as pgui
from selenium.webdriver.common.by import By
from config import LIKE_AMOUNT

dt = datetime.datetime

def now():
    return dt.now().strftime("%m/%d %H:%M:%S")

def likeLike(driver, keyword=""):
    n = 0
    n_all = 0
    n_interval = 100
    try_count = range(150)
    is_except_count_error = False
    
    try:
        for _ in try_count:
            try:
                driver.find_elements(By.CSS_SELECTOR, '._acut')[4].click() # Header heart mark
                for _ in try_count:
                    try:
                        driver.find_element(By.CSS_SELECTOR, '._aa61')
                        break
                    except:
                        print('No ._aa61')
                        sleep(0.2)
                        pass
                driver.refresh()
                break
            except:
                print('No ._acut')
                sleep(0.2)
                pass
            
        for _ in try_count:
            try:
                driver.find_elements(By.CSS_SELECTOR, '._acut')[0]  # Headers
                for _ in range(2):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(0.1)
                break
            except:
                sleep(0.2)
                pass
            
        print(driver.find_elements(By.CSS_SELECTOR, '._aagw'))
        driver.find_elements(By.CSS_SELECTOR, '._aagw')[8].click() # First post
        sleep(2)
        old_n = 0
        n_interval_countdown = n_interval
        
        old_mouse_position = pgui.position()
        print('-'*100)
        print("Start Time:", now())
        while n < LIKE_AMOUNT:
            try:
                btns = driver.find_elements(By.CSS_SELECTOR, '._abl-')
                like_btn = btns[5]
                is_unliked = len(like_btn.find_elements(By.XPATH, "div")) == 2
                if is_unliked:
                    if uniform(0, 1) <= 0.8:
                        like_btn.click()
                
                n += 1
                if n % 5 == 0:
                    back_btn = btns[2]
                    back_btn.click()
                    next_btn = btns[3]
                    next_btn.click()
                sleep(0.1)
            except Exception:
                n_interval_countdown -= 1
                
            try:
                next_btn = btns[3]
                next_btn.click()
                n_all += 1
                except_count = 0
            except:
                driver.execute_script("arguments[2].click();", btns)
                n_all += 1
                print(n, ": Exception Proceeding executed!!")
                except_count += 1
                
            sleep(0.1)
            
            if except_count >= 10:
                is_except_count_error = True
                raise ValueError("`except_count` exceeded 10!!")

            if n_interval_countdown < 0:
                print("interval: "+str(n))
                
                if old_mouse_position == pgui.position() and old_n == n:
                    pgui.press('shift')
                    pass
                else:
                    old_mouse_position = pgui.position()
                    old_n = n
                    
                sleep(2)
                n_interval_countdown = n_interval
            n_interval_countdown -= 1
            
            sleep(2.1)

        print('Done successfully!')
    
    except Exception:
        traceback.print_exc()

    if 'n' in locals():
            print(f"{keyword}, liked: {n}")
            print(f"n_all: {n_all}")
            print("End Time:", now())
            print('-'*100)

    return is_except_count_error