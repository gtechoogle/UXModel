from app_init import AppInit
import json

def main():
    # AppInit("F:\\Github\\UXModel\\testApk\\news_article\\testApk\\news_article.apk").first_run(steps_info="")
    file_path = "F:\\Github\\UXModel\\testApk\\news_article\\config.json"
    with open(file_path, 'r', encoding='utf-8') as file:
        raw = json.load(file)
        print (raw)
if __name__ == "__main__" :
    main()
