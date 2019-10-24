from init.Base import Base
import Page as p
class Page_Phone(Base):
    def phone_add(self):
        self.click_element(p.phone_add)

    def phone_inputname(self,text):
        self.input_element(p.phone_text_name,text)

    def phone_inputnumber(self,text):
        self.input_element(p.phone_text_number,text)

    def phone_back(self):
        self.click_element()

    def phong_b(self):
        return self.find_element(p.phone_p)