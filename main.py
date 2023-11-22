from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.service import Service
import sys
from fake_useragent import UserAgent
import time
import getMailCode
import getInfo


def find_element_by_text(driver, tag_name, text):
    xpath_expression = f"//{tag_name}[contains(text(), '{text}')]"
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_expression)))


def click_element_with_retry(element, max_retries=3):
    for _ in range(max_retries):
        try:
            element.click()
            return True  # Si le clic réussit, sortir de la boucle
        except Exception as e:
            print(f"Erreur lors du clic : {str(e)}")
            time.sleep(1)  # Attendre une seconde avant de réessayer

    print(f"Impossible de cliquer sur l'élément après {max_retries} tentatives.")
    return False

def fill_date_of_birth(driver):
    day = str(random.randint(1, 26))
    month = str(random.randint(1, 12))
    year = str(random.randint(22, 50))
    print(day)
    print(month)
    print(year)
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][1]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][1]/select/option[{month}]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][2]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][2]/select/option[{day}]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][3]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f"//span[@class='_aav3'][3]/select/option[{year}]"))).click()
    except Exception as e:
        print(f"Erreur lors du remplissage de la date de naissance : {str(e)}")
        sys.exit()


def load_page():
    options = Options()
    # options.add_argument('--user-data-dir=C:/Users/samada/AppData/Local/Google/Chrome/User Data')
    # options.add_argument('--profile-directory=Default')
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.instagram.com/accounts/emailsignup/")
    WebDriverWait(driver,10000).until(EC.visibility_of_element_located((By.CLASS_NAME,'_a9--')))
    accept_cookies = driver.find_element(By.CLASS_NAME, "_a9--")
    accept_cookies.click()
    inputs = {
        "email" : driver.find_element("name", "emailOrPhone"),
        "name" : driver.find_element("name", "fullName"),
        "username" : driver.find_element("name", "username"),
        "password" : driver.find_element("name", "password")
    }
    user = getInfo.generate_user()
    form = {
        "email" : user["email"],
        "name" : user["nom"] + " " + user["prenom"],
        "username" : user["username"],
        "password" : user["password"]
    }
    for input_name, input_field in inputs.items():
        if input_field:
            print(f"click on {input_name}")
            click_element_with_retry(input_field)
            input_field.send_keys(form[input_name])
    
    time.sleep(1)
    try:
        refresh_btns = driver.find_element(By.XPATH, "//button[@class=' _acan _acao _acas _aj1- _ap30']")
        refresh_btns.click()
    except():
        pass
        
    time.sleep(2)
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
    submit_btn.click()
    time.sleep(1)
    fill_date_of_birth(driver)
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
    submit_btn.click()
    code = getMailCode.get_mail_code(user["email"], driver)
    input_code_field = driver.find_element("name", "email_confirmation_code")
    input_code_field.send_keys(code)
    submit_code_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@class="x1i10hfl xjqpnuy xa49m3k xqeqjp1 x2hbi6w x972fbf xcfux6l x1qhh985 xm0m39n xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x18d9i69 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x1lku1pv x1a2a7pz x6s0dn4 xjyslct x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1ejq31n xd10rxx x1sy0etr x17r0tee x9f619 x9bdzbf x1ypdohk x1f6kntn xwhw2v2 x10w6t97 xl56j7k x17ydfre x1swvt13 x1pi30zi x1n2onr6 x2b8uid xlyipyv x87ps6o xcdnw81 x1i0vuye xh8yej3 x1tu34mt xzloghq x3nfvp2"]'))
    )

    # Cliquer sur l'élément
    submit_code_btn.click()
    print(code)
    time.sleep(60)
    driver.quit()
    
load_page()