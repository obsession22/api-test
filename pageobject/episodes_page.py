import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from config.config_util import get_yaml_config
from pageobject.table_commit import LoginPage

# 导航栏元素
# 剧集管理
episodes_mg_title_key = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[6]')
# 剧集
episodes_title_key = (By.XPATH, '//*[@id="sideMenu"]/div/ul/li[6]/dl/dd[2]/a')

# 页面元素
episodes_iframe = (By.XPATH, '//*[@id="353"]')
episodes_add_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[1]')

# 新增页面
episodes_iframe2 = (By.XPATH, '//*[@id="layui-layer-iframe2"]')
episodes_add_name = (By.XPATH, '//*[@id="name"]')
cover_button = (By.XPATH, '/html/body/form/div[1]/div/div/div[2]/div/div[2]/div[2]')
tips_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[12]/div/div/xm-select')
tips = (By.XPATH, '/html/body/form/div[1]/div/div/div[12]/div/div/xm-select/div[3]/div/div/div[2]/div/div')
desc_key = (By.XPATH, '//*[@id="desc"]')
sort_key = (By.XPATH, '//*[@id="sort"]')
cate_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[5]/div/div')
cate_next_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[5]/div/div/xm-select/div[3]/div/div/div[2]/div/div')
price_key =(By.XPATH, '//*[@id="price"]')
vip_price_key =(By.XPATH, '//*[@id="vip_price"]')
number_key = (By.XPATH, '//*[@id="total_num"]')
wx_drama_id_key = (By.XPATH, '//*[@id="wx_drama_id"]')
hide_key = (By.XPATH, '/html/body/form/div[1]/div/div/div[10]/div/div/em')
state_key =(By.XPATH, '/html/body/form/div[1]/div/div/div[11]/div/div/em')
submit_key = (By.XPATH, '/html/body/form/div[2]/div/button[1]')

# 封面iframe
cover_iframe = (By.CSS_SELECTOR, '#layui-layer-iframe2')
id_key = (By.XPATH, '/html/body/div[2]/div/div/div[2]/div[3]/div[2]/table/tbody/tr[3]/td[1]/div')
ok_button = (By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/button[2]')


# 剧集页面
class EpisodesPage(BasePage):
    # 新增剧集
    def add_episodes(self, episodes_name, desc, sort, cate_id, price, vip_price, number, wx_drama_id, hide, state):
        LoginPage.login(self)
        self.click(episodes_mg_title_key)
        time.sleep(1)
        self.click(episodes_title_key)
        self.goto_frame(episodes_iframe)
        self.click(episodes_add_button)
        time.sleep(1)
        # 切换到下一级iframe
        self.goto_frame(episodes_iframe2)
        if episodes_name != 'null':
            self.send_keys(episodes_add_name, episodes_name)
        self.click(cover_button)
        print(cover_iframe)
        self.goto_frame(cover_iframe)
        self.click(id_key)
        self.click(ok_button)
        # 返回上一级
        self.out_frame_parent()
        if desc != 'null':
            self.clear(desc_key)
            self.send_keys(desc_key, desc)
        if sort != 'null':
            self.clear(sort_key)
            self.send_keys(sort_key, sort)
        # if cate_id != 'null':
        #     self.send_keys()
        self.click(cate_key)
        self.click(cate_next_key)
        if price != 'null':
            self.clear(price_key)
            self.send_keys(price_key, price)
        if vip_price != 'null':
            self.clear(vip_price_key)
            self.send_keys(vip_price_key, vip_price)
        if number != 'null':
            self.clear(number_key)
            self.send_keys(number_key, number)
        if wx_drama_id != 'null':
            self.clear(wx_drama_id_key)
            self.send_keys(wx_drama_id_key, wx_drama_id)
        if hide == 1:
            self.click(hide_key)
        if state == 1:
            self.click(state_key)
        self.click(tips_key)
        self.click(tips)
        self.click(submit_key)



