from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from notification_sender import send_push_notification_success

SECONDS_IN_DAY = 86400


def check_next_week():
        
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        USER_ID = 'USERNAME'
        PASSWORD = 'PASSWORD'
        driver = webdriver.Chrome(PATH)

        driver.get("https://psschedule.reflexisinc.co.uk/wfmmcdirlprd/rws/ess/ess_notice_board.jsp?mm=ESS")

        num = driver.find_element_by_name("txtUserID")
        num.send_keys(USER_ID)

        password = driver.find_element_by_name("txtPassword")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.RETURN)

        next_week = driver.find_element_by_id("rightImg")

        if next_week.is_displayed():
            send_push_notification_success()
            driver.quit()
            sleep(SECONDS_IN_DAY)
            check_next_week()
        else:
            sleep(SECONDS_IN_DAY/24)        
            check_next_week()
            

if __name__ == "__main__":
    check_next_week()