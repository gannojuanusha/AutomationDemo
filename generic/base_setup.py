#from webbrowser import Chrome
#from openpyxl.comments.comment_sheet import Properties
from pyjavaproperties import Properties
import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote

class BaseSetup:
    @pytest.fixture(autouse=True)
    def precondition(self):
        pptobj=Properties()
        pptobj.load(open('config.properties'))
        self.xl_path=pptobj['XL_PATH']
        print("Excelpath",self.xl_path)
        usegrid=pptobj['USEGRID'].lower()
        print("use grid",usegrid)
        gridurl=pptobj['GRIDURL']
        print("grid url",gridurl)
        appurl=pptobj['APPURL']
        browser=pptobj['BROWSER'].lower()
        print('browser',browser)
        ito=pptobj['IMPLICIT_TIME_OUT']
        eto=pptobj['EXPLICIT_TIME_OUT']
        
        if usegrid=="yes":
            print("executing in remote system")
            if browser=='chrome':
                self.driver=Remote(gridurl,DesiredCapabilities.CHROME)
            elif browser=='firefox':
                self.driver=Remote(gridurl,DesiredCapabilities.FIREFOX)
            else:
                self.driver=Remote(gridurl,DesiredCapabilities.EDGE)
        else:
            print("executing in local system")
            if browser=='chrome':
                print("open in chrome browser")
                self.driver=webdriver.Chrome()
            elif browser=='firefox':
                print("open in firefox browser")
                self.driver=webdriver.Firefox()
            else:
                print("open in edge browser")
                self.driver=webdriver.Edge() 
        self.driver.get(appurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(ito)
        self.wait=WebDriverWait(self.driver,eto)
    @pytest.fixture(autouse=True)    
    def postcondition(self):
        yield
        print("Close the browser")
        self.driver.quit()

