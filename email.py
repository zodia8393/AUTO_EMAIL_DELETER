from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(driver):
    # 네이버 이메일 로그인 페이지로 이동
    naver_login_url = 'https://nid.naver.com/nidlogin.login'
    driver.get(naver_login_url)

    # 로그인 정보 입력
    driver.find_element_by_name('id').send_keys('네이버 이메일 아이디')
    driver.find_element_by_name('pw').send_keys('네이버 이메일 비밀번호')
    driver.find_element_by_css_selector('.btn_global').click()

def delete_email():
    # 크롬 드라이버 실행
    driver = webdriver.Chrome('/path/to/chromedriver')
    driver.get('https://www.naver.com')

    # 네이버 이메일 로그인
    login(driver)

    # 이메일 페이지로 이동
    naver_email_url = 'https://mail.naver.com/'
    driver.get(naver_email_url)

    # 오늘 온 메일이 아닌 모든 메일 삭제
    driver.find_element_by_id('list_for_select').find_element_by_css_selector('._list_select_all').click()
    driver.find_element_by_id('btnMain').find_element_by_css_selector('.btn_all').click()
    driver.switch_to.alert.accept()

    # 브라우저 종료
    driver.quit()

def empty_trash():
    # 크롬 드라이버 실행
    driver = webdriver.Chrome('/path/to/chromedriver')
    driver.get('https://www.naver.com')

    # 네이버 이메일 로그인
    login(driver)

    # 이메일 페이지로 이동
    naver_email_url = 'https://mail.naver.com/'
    driver.get(naver_email_url)

    # 메일 휴지통으로 이동
    driver.find_element_by_css_selector('#gnb_menu .group_mail').click()
    driver.find_element_by_css_selector('.name_trash').click()

    # 메일 휴지통 모두 삭제
    driver.find_element_by_id('list_for_select').find_element_by_css_selector('._list_select_all').click()
    driver.find_element_by_id('btnMain').find_element_by_css_selector('.btn_all').click()
    driver.switch_to.alert.accept()

    # 브라우저 종료
    driver.quit()
