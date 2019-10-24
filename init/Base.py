from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element(self,loc,timeout=5,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*loc))

    def click_element(self,loc):
        self.find_element(loc).click()

    def input_element(self,loc,text):
        self.find_element(loc).send_keys(text)

