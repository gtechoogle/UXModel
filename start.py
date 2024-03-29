from app_init import AppInit
from app_test import AppTest
import json
import os

def main():
    test_file = os.path.join(os.getcwd(),'testApk/news_article/config.json')
    with open(test_file, 'r', encoding='utf-8') as file:
        raw = json.load(file)
    print(raw['apk_path'])
    # AppInit(raw).first_run(steps_info=raw['launch_step'])
    AppTest(raw).launch_test(app_name = raw['app_name'])

if __name__ == "__main__" :
    main()
