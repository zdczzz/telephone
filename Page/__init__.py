from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

phone_add=(By.ID,'com.android.contacts:id/floating_action_button')
phone_text_name=(By.XPATH,"//*[@text='姓名']")
phone_text_number = (By.XPATH,"//*[@text='电话']")

phone_p = (By.ID,'com.android.contacts:id/photo_touch_intercept_overlay')

# by=MobileBy.ACCESSIBILITY_ID, value=accessibility_id