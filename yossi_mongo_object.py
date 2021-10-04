from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class YossiMongoObject(object):
    __mongo_driver = None
    __site_driver = None
    __options = None
    __mail = None
    __url = None
    __title = None

    def __init__(self):
        self.set_up_driver()
        self.__mongo_driver.get("http://localhost:8080/")
        self.__site_driver.get("http://localhost:3000/")
        self.__mongo_driver.implicitly_wait(1)
        self.__site_driver.implicitly_wait(1)

    def set_up_driver(self):
        self.__options = Options()
        self.setUpOptions(self.__options)
        self.__mongo_driver = webdriver.Chrome(options=self.__options)
        self.__site_driver = webdriver.Chrome(options=self.__options)
        self.__url = self.__mongo_driver.current_url
        self.__title = self.__mongo_driver.title

    def setUpOptions(self, options):
        options.add_argument("--disable_extensions")
        options.add_argument("--incognito")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--start-maximized")

    def navigate_to_mongo_express_mail(self):
        # time.sleep(5)

        self.__mongo_driver.find_element_by_css_selector("body > div > div:nth-child(2) > div > div.panel.panel-default > div.panel-body.no-padding > table > tbody > tr:nth-child(4) > td:nth-child(2) > h3 > a").click()
        self.__mongo_driver.find_element_by_css_selector("body > div > div:nth-child(2) > div > div:nth-child(1) > div.panel-body.no-padding > table > tbody > tr:nth-child(2) > td:nth-child(5) > h3 > a").click()
        self.__mail = self.__mongo_driver.find_element_by_css_selector("body > div > div:nth-child(2) > div > div.table-responsive.tableWrapper > table > tbody > tr > td:nth-child(3) > div").text

    def edit_mongo_mail(self, string):
        self.__site_driver.find_element_by_css_selector("#container > button").click()
        action = ActionChains(self.__site_driver)
        action.double_click(self.__site_driver.find_element_by_css_selector("#input-email"))
        action.key_down(Keys.CONTROL)
        action.send_keys("a")
        action.key_up(Keys.CONTROL)
        action.send_keys(string)
        action.perform()
        self.__site_driver.find_element_by_css_selector("#container-edit > button").click()


    def get_mongo_express_mail(self):
        return self.__mail

    def get_mongo_driver(self):
        return self.__mongo_driver

    def get_site_driver(self):
        return self.__site_driver

if __name__ == "__main__":
    b = YossiMongoObject()
    b.edit_mongo_mail("yossigoldberg2@gmail.com")

    b.navigate_to_mongo_express_mail()
    print(b.get_mongo_express_mail())
    b.get_mongo_driver().quit()
    b.get_site_driver().quit()
#
#