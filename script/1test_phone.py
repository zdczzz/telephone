from selenium.webdriver.support.wait import WebDriverWait
# import allure
from init.init_driver import init_driver
from Page.page_phone import Page_Phone
import pytest
import time
from init.read_yaml import read_yam
def yaml_data():
    dt = read_yam('data1').get('Data')
    dt_list = []
    for i in dt.values():
        dt_list.append(i.values())
    return dt_list

class Test_phone():
    def setup_class(self):
        self.driver = init_driver()
        self.pp = Page_Phone(self.driver)

    def teardown_class(self):
        self.driver.quit()



    @pytest.mark.parametrize('name,number',yaml_data())
    def test_input(self,name,number):
        self.pp.phone_add()
        self.pp.phone_inputname(name)
        self.pp.phone_inputnumber(number)
        back = WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_accessibility_id('向上导航'))
        back.click()
        try:
            self.pp.phong_b()
            self.driver.back()
        except:
            return self.test_input

if __name__ == '__main__':
    pytest.main()
