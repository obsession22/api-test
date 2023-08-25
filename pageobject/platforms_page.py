import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.config_util import get_yaml_config
from pageobject.table_commit import LoginPage

platform_title = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[7]')
link_title = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[7]/dl/dd[2]/a')
link_iframe = (By.XPATH, '//*[@id="384"]')
query_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button')
ID_key = (By.XPATH, '//*[@id="id"]')
vedio_id_key = (By.XPATH, '//*[@id="vid"]')
episodes_id_key = (By.XPATH, '//*[@id="eid"]')
user_id_key = (By.XPATH, '//*[@id="show_id"]')
set_id_key = (By.XPATH, '//*[@id="return_id"]')
pay_id_key = (By.XPATH, '//*[@id="recharge_temp"]')
query_button_key = (By.XPATH, '//*[@id="search-form"]/div/form/div/div[7]/button[1]')


class PlatformPage(BasePage):
    # 查询推广链接
    def query_promotions(self,ID, vedio_id, episodes_id, user_id, set_id, pay_id):
        LoginPage.login(self)
        self.click(platform_title)
        time.sleep(2)
        self.click(link_title)
        self.goto_frame(link_iframe)
        time.sleep(1)
        self.click(query_button)
        if ID != 'null':
            self.send_keys(ID_key, ID)
        if vedio_id != 'null':
            self.send_keys(vedio_id_key, vedio_id)
        if episodes_id != 'null':
            self.send_keys(episodes_id_key, episodes_id)
        if user_id != 'null':
            self.send_keys(user_id_key, user_id)
        if set_id != 'null':
            self.send_keys(set_id_key, set_id)
        if pay_id != 'null':
            self.send_keys(pay_id_key, pay_id)
        self.click(query_button_key)






