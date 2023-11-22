import time

def get_mail_code(email, driver):
    fMail = email.split("@")
    print(fMail)
    mailName = fMail[0]
    domain = fMail[1]
    INST_CODE = 'https://email-fake.com/' + domain + '/' + mailName
    
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(INST_CODE)

    t = driver.title

    while True:
        if t[:4]=="Fake":
            driver.refresh()
            t = driver.title
            print(t)
            time.sleep(1)
        else:
            break

    code = t[:6]
    driver.switch_to.window(driver.window_handles[0])
    return code