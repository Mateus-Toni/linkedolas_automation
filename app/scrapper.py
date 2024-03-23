from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import parameters

import time

def get_driver(url):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get(url)

    return driver


def get_element_by_xpath(driver, xpath):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))
    )

    return element


def get_element_by_css_selector(driver, css_selector):

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )

    return element

def click_element_by_xpath(driver, xpath):

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()


def click_element_by_class_name(driver, name):

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, name))).click()


def click_element_by_css_selector(driver, css_selector):

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click()


def login_linkedin(driver):

    driver.delete_all_cookies()
    
    driver.execute_script("window.localStorage.clear();")
    driver.execute_script("window.sessionStorage.clear();")
    driver.execute_script("window.open('','_cache').close();")

    driver.get(parameters.URL_LOGIN_LINKEDIN)

    email_field = get_element_by_xpath(driver, parameters.XPATH_LOGIN_FIELD)
    pwd_field = get_element_by_xpath(driver, parameters.XPATH_PWD_FIELD)

    email_field.send_keys(parameters.EMAIL_LOGIN_LINKEDIN)
    pwd_field.send_keys(parameters.PWD_LOGIN_LINKEDIN)

    click_element_by_xpath(driver, parameters.XPATH_LOGIN_BUTTON)

    while True:

        if driver.current_url == parameters.URL_FEED_LINKEDIN:
            
            print('while break')

            break


def get_list_connections(page):

    list_conn = []

    page_html = BeautifulSoup(page, "html.parser")

    list_item_connection = page_html.find_all('li', class_=parameters.CSS_SELECTOR_LI_PROFILES)

    for item in list_item_connection:
                                              
        name_lead = (item.find('span', class_=parameters.CSS_SELECTOR_NAME_PROFILE).text).strip()
        
        url_user = item.find('a', class_=parameters.CSS_SELECTOR_URL_PROFILE).get('href')
        url_user = parameters.URL_HOME_LINKEDIN + url_user

        is_open_to_work = item.find('img').get('alt')
        is_open_to_work = 'está buscando emprego' in is_open_to_work

        list_conn.append({
            "name": name_lead,
            "url": url_user,
            "open_to_work": is_open_to_work
        })

    return list_conn
        

def send_menssage_for_list_conections(driver, url, menssage):

    driver.get(url)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, parameters.CSS_SELECTOR_DIV_PROFILES))
    )

    list_connections = get_list_connections(driver.page_source)

    list_connections = [{'name': 'Amanda Alencar', 'url': 'https://www.linkedin.com/in/amanda-alencar-3750b11a3/'}]

    for lead in list_connections:

        driver.get(lead['url'])

        click_element_by_xpath(driver, parameters.XPATH_OPEN_MENSSAGE_BUTTON)

        menssage_field = get_element_by_xpath(driver, parameters.XPATH_MENSSAGE_FIELD)
        menssage_field.send_keys(menssage)

        click_element_by_xpath(driver, parameters.XPATH_SEND_MENSSAGE_BUTTON)

        time.sleep(1)

        click_element_by_xpath(driver, parameters.XPATH_CLOSE_MENSSAGE_BOX)
        


