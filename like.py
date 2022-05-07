import os
import ctypes

from likeChrome import likeChrome
from config import USERNAMES, PASSWORDS, SOUND_PATH


def main():
    print(USERNAMES)
    lists_num = input('【ユーザー番号(半角数字)】')
    if lists_num == "":
        lists_num = 0
    user_name = USERNAMES[int(lists_num)]
    password = PASSWORDS[int(lists_num)]
    print(user_name+"で実行します")
    keywords = input('【       Key Word       】')
    if keywords == "":
        print("後でキーワードを入力してください")

    shutdown_confirm = input("【終了後にスリープ/シャットダウンしますか？[s/u]】")
    print("！！音量を確認してください！！")

    likeChrome(keywords=keywords.split(), user_name=user_name, password=password)
    
    from playsound import playsound
    playsound(SOUND_PATH)
    
    shutdownOrSleep(shutdown_confirm=shutdown_confirm)

def shutdownOrSleep(shutdown_confirm):
        SorU = str.lower(shutdown_confirm)
        if SorU == "s":
            ctypes.windll.powrprof.SetSuspendState(0, 0, 0)
        elif SorU == "u":
            os.system('shutdown -s -t 0')

if __name__ == "__main__":
    main()