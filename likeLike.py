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
            if driver.find_elements(By.CSS_SELECTOR, '._acf_'): break # Header heart mark
            
        for _ in try_count:
            if driver.find_elements(By.CSS_SELECTOR, '._aagw'): break
            sleep(0.2)

        driver.find_elements(By.CSS_SELECTOR, '._aagw')[11].click() # Third post
        sleep(2)
        old_n = 0
        n_interval_countdown = n_interval
        
        old_mouse_position = pgui.position()
        print('-'*100)
        print("Start Time:", now())
        while n < LIKE_AMOUNT:
            try:
                btns = driver.find_elements(By.CSS_SELECTOR, '._abl-')
                like_btn = btns[3]
                is_unliked = len(like_btn.find_elements(By.XPATH, "div")) == 2
                if is_unliked:
                    if uniform(0, 1) <= 0.8:
                        like_btn.click()
                
                n += 1
                if n % 5 == 0:
                    back_btn = btns[0]
                    back_btn.click()
                    next_btn = btns[1]
                    next_btn.click()
                sleep(0.1)
            except Exception:
                n_interval_countdown -= 1
                
            try:
                next_btn = btns[1]
                next_btn.click()
                n_all += 1
                except_count = 0
            except:
                driver.execute_script("arguments[3].click();", btns)
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