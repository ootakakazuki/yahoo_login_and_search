# yahooにログインして標準入力から受け取った文字を検索する半自動スクリプト

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def start_chrome():
    # Chrome起動
    driver = webdriver.Chrome()
    driver.maximize_window() # 画面サイズ最大化

    url = 'https://login.yahoo.co.jp/config/login'
    driver.get(url)

    return driver

def login_google(driver, login_id, login_pw):

    #最大待機時間（秒）
    wait_time = 10

    ### IDを入力
    login_id_xpath = '//*[@id="btnNext"]'
    # xpathの要素が見つかるまで待機します。
    WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.XPATH, login_id_xpath)))
    driver.find_element_by_name("login").send_keys(login_id)
    driver.find_element_by_xpath(login_id_xpath).click()

    ### パスワードを入力
    login_pw_xpath = '//*[@id="btnSubmit"]'
    # xpathの要素が見つかるまで待機します。
    time.sleep(6) # クリックされずに処理が終わるのを防ぐために追加。

    driver.find_element_by_name("passwd").send_keys(login_pw)
    driver.find_element_by_xpath(login_pw_xpath).click()

    # 検索したいワードの入力と検索ボタンの押下
    time.sleep(5)
    login_pw_name = '//*[@class="_63Ie6douiF2dG_ihlFTen rapid-noclick-resp"]'
    driver.find_element_by_name("p").send_keys(search_word)
    driver.find_element_by_xpath(login_pw_name).click()

if __name__ == '__main__':
    
    #ログイン情報
    login_id = input("please input your id:")
    login_pw = input("please input your password:")
    search_word = input("Please input word you wanna search")
    
	# Chromeを起動
    driver = start_chrome()

    # Yahooにログイン
    login_google(driver, login_id, login_pw, search_word)
