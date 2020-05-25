from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
class Base():
    def __init__(self,driver):
        self.driver=driver
    #定位元素
    def find(self,locator):
        '''locator=('id','kw')
        id\xpath\link text\partical link text\name\tag name\class name\css selector
        '''
        try:
            element=WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element(*locator))
            return element
        except:
            return "没有找到元素"
    #判断元素是否存在
    def is_element_exist(self,locator):
        try:
            self.find(locator)
            return True
        except:
            return False

    #定位一组元素
    def find(self,locator):
        '''locator=('id','kw')
        id\xpath\link text\partical link text\name\tag name\class name\css selector
        '''
        elements=WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_elements(*locator))
        return elements
    #选中元素
    def selected(self,locator):
        select=self.find(locator)
        Select(select).select_by_index(2)#选第3个
        select.click()
    #判断元素是否被选中
    def selected_status(self,locator):
        r = self.find(locator)
        status=r.is_selected()
        return status

    #输入方法
    def send(self,locator,text):
        self.find(locator).send_keys(text)
    #点击元素的方法
    def click(self,locator):
        self.find(locator).click()
    #判断元素中是否包含文本
    def text_in_element(self,locator,text,timeout=10):
        try:
            WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
            return True
        except TimeoutException:
            return False
    #判断是否有alert
    def is_alert_present(self,timeout=10):
        '''有返回alert，没有返回False'''
        result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
        return result
    #鼠标悬停操作
    def move_to_element(self,locator):
        element=self.find(locator)
        ActionChains(self.driver).move_to_element(element).perform()
if __name__=='__main__':
    driver=webdriver.Chrome()
    driver.get("http://baidu.com")
    loc=('id','kw')
    base=Base(driver)
    base.send(loc,'北京')
