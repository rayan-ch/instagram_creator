from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time

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

def fill_date_of_birth(driver, day, month, year):
    try:
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][1]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][1]/select/option[4]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][2]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][2]/select/option[4]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][3]/select"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='_aav3'][3]/select/option[4]"))).click()

    except Exception as e:
        print(f"Erreur lors du remplissage de la date de naissance : {str(e)}")


def load_page():
    driver = webdriver.Chrome()
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
    form = {
        "email" : "jdujbndz@gmail.com",
        "name" : "dsdzdzd ijnoan",
        "username" : " obaodap54",
        "password" : "sdDIJODIPADPOAJ?D"
    }
    for input_name, input_field in inputs.items():
        if input_field:
            print(f"click on {input_name}")
            click_element_with_retry(input_field)
            input_field.send_keys(form[input_name])
    
    time.sleep(3)
    refresh_btns = driver.find_element(By.XPATH, "//button[@class='_acan _acao _acas _aj1- _ap30']")
    if refresh_btns:
        refresh_btns.click()
    time.sleep(5)
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Suivant')]")
    submit_btn.click()
    time.sleep(3)
    fill_date_of_birth(driver, "5", "mars", "1990")
    print(submit_btn)
    time.sleep(15)
    driver.quit()
    
load_page()