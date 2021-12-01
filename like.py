import os
import ctypes
from playsound import playsound
from likeChrome import likeChrome


def main():
    
    user_names = ["hoboki.jp", "naniwatoukeigaku", "soymafia_osaka"]
    passwords =["ki2064/", "wpyrki", "2064kichi"]
    print(user_names)
    lists_num = input('【ユーザー番号(半角数字)】')
    if lists_num == "":
        lists_num = 0
    user_name = user_names[int(lists_num)]
    password = passwords[int(lists_num)]
    print(user_name+"で実行します")
    keywords = input('【       Key Word       】')
    if keywords == "":
        print("後でキーワードを入力してください")

    shutdown_confirm = input("【終了後にスリープ/シャットダウンしますか？[s/u]】")

    print("！！音量を確認してください！！")

    likeChrome(keywords=keywords.split(), user_name=user_name, password=password)
    
    playsound(os.getcwd() + '\pinpon.mp3')
    
    shutdownOrSleep(shutdown_confirm=shutdown_confirm)

def shutdownOrSleep(shutdown_confirm):
        SorU = str.lower(shutdown_confirm)
        if SorU == "s":
            ctypes.windll.powrprof.SetSuspendState(0, 0, 0)
        elif SorU == "u":
            os.system('shutdown -s -t 0')

if __name__ == "__main__":
    main()