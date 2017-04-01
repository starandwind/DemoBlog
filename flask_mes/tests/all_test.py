import unittest
from selenium import webdriver

#before running this, you should first run run_test_server.py,and
#you can run this only once before you restart run_test_server.py

class TestURLs(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_index(self):
        #check the index page
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn("register",self.driver.page_source)
        self.assertIn("login",self.driver.page_source)
        
    def test_register_and_logout(self):
        
        #try to register
        self.driver.get("http://127.0.0.1:5000/register")
        username = self.driver.find_element_by_name("username")
        username.send_keys("testuser")
        passwd = self.driver.find_element_by_name("passwd")
        passwd.send_keys("testpasswd")
        submit = self.driver.find_element_by_id("submit")
        submit.click()

        #check the changed index correction
        self.assertIn("mypage",self.driver.page_source)
        self.assertIn("logout",self.driver.page_source)
        self.assertIn("publish",self.driver.page_source)

    def test_login_and_publish_and_delete(self):
        #try to login through added user
        self.driver.get("http://127.0.0.1:5000/login")
        username = self.driver.find_element_by_name("username")
        username.send_keys("testlogin")
        passwd = self.driver.find_element_by_name("passwd")
        passwd.send_keys("testpasswd")
        submit = self.driver.find_element_by_id("submit")
        submit.click()

        #go to publish page
        self.assertIn("publish",self.driver.page_source)
        publish = self.driver.find_element_by_id("publish")
        publish.click()

        #try to publish a post
        title = self.driver.find_element_by_name("title")
        title.send_keys("test title")
        passwd = self.driver.find_element_by_name("text")
        passwd.send_keys("test text")
        submit = self.driver.find_element_by_id("submit")
        submit.click()

        #check the people page
        self.assertIn("test title",self.driver.page_source)
        self.assertIn("test text",self.driver.page_source)
        self.assertIn("delete",self.driver.page_source)

        #try to delete the post and check it
        self.driver.get("http://127.0.0.1:5000")
        self.assertIn("test title",self.driver.page_source)
        self.assertIn("test text",self.driver.page_source)
        delete = self.driver.find_element_by_id("delete")
        delete.click()
        self.assertNotIn("test title",self.driver.page_source)
        self.assertNotIn("test text",self.driver.page_source)
        

if __name__=='__main__':
    unittest.main()
