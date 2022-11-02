import sys
import argparse
import os
import random
import ctypes
from distutils.util import strtobool

from likeChrome import likeChrome
from config import *


def main(args):
    if args.auto:
        username = USERNAMES[args.user]
        password = PASSWORDS[args.user]
        keywords = random.choice(KEYWORDS)
        shutdown_confirm = ""
    else:
        print(USERNAMES)
        lists_num = input('【ユーザー番号(半角数字)】')
        if lists_num == "":
            lists_num = 0
        username = USERNAMES[int(lists_num)]
        password = PASSWORDS[int(lists_num)]
        print(username+"で実行します")
        keywords = input('【       Key Word       】')
        if keywords == "":
            print("後でキーワードを入力してください")
        shutdown_confirm = input("【終了後にスリープ/シャットダウンしますか？[s/u]】")
    
    likeChrome(keywords=keywords.split(), username=username, password=password)
    if ENABLE_FINISH_SOUND:
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
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--auto',
        type=strtobool,
    )
    parser.add_argument(
        '--user',
        type=int,
    )
    args = parser.parse_args()
    
    main(args)