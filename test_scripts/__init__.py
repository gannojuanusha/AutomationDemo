from generic.base_setup import BaseSetup

class Test_Script1(BaseSetup):
    def test_script1(self):
        print("this is test script1")
        print(self.driver.title)