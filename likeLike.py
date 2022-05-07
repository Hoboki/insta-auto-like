import datetime
from time import sleep
import traceback
from random import uniform
import pyautogui as pgui


dt = datetime.datetime

def now():
    return dt.now().strftime("%m/%d %H:%M:%S")

def likeLike(driver, keyword=""):
    n = 0
    n_all = 0
    n_interval = 100
    like_amount = 0
    try_count = range(150)
    
    try:
        for _ in try_count:
            try:
                driver.find_elements_by_css_selector('._0ZPOP')[0].click()
                for _ in try_count:
                    try:
                        driver.find_element_by_css_selector('.PUHRj')
                        break
                    except:
                        sleep(0.2)
                        pass
                driver.refresh()
                break
            except:
                sleep(0.2)
                pass
            
        for _ in try_count:
            try:
                driver.find_elements_by_css_selector('._0ZPOP')[0]
                for _ in range(2):
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    sleep(0.1)
                break
            except:
                sleep(0.2)
                pass

        driver.find_elements_by_css_selector('._9AhH0')[9].click()
        sleep(2)
        old_n = 0
        n_interval_countdown = n_interval
        is_except_count_error = False
        old_mouse_position = pgui.position()
        print('-'*100)
        print("　"*5+"！"*21)
        print("　"*5+"！！！！！音量を確認してください！！！！！")
        print("　"*5+"！"*21)
        print("Start Time:", now())
        while n < like_amount:
            try:
                btns = driver.find_elements_by_css_selector('.wpO6b')
                like_btn = btns[5]
                is_unliked = len(like_btn.find_elements_by_xpath("div")) == 2
                if is_unliked:
                    sleep(uniform(0, 0.5)) # Randomize like speed
                    like_btn.click()
                    pass
                
                n += 1
                sleep(0.1)
            except Exception:
                n_interval_countdown -= 1
                
            try:
                next_btn = btns[3]
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
            
            sleep(1)

        print('Done successfully!')
    
    except Exception:
        traceback.print_exc()

    if 'n' in locals():
            print(f"{keyword}, liked: {n}")
            print(f"n_all: {n_all}")
            print("End Time:", now())
            print('-'*100)

    return is_except_count_error