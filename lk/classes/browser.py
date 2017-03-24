from time import sleep
from lk.classes.utils.test_util import TestUtil
from selenium.common.exceptions import ElementNotVisibleException, StaleElementReferenceException
from selenium import webdriver
# from share.classes.env_util import EnvUtil
import splinter
import six
from splinter.exceptions import ElementDoesNotExist


class Browser(object):

    def __init__(self, wait_time=15):

        # http://stackoverflow.com/questions/15165593/set-chrome-prefs-with-python-binding-for-selenium-in-chromedriver
        # chrome_options = Options()
        # chrome_options.add_experimental_option("prefs", {'profile.managed_default_content_settings.images': 2})
        # chrome = webdriver.Chrome('/path/to/chromedriver', chrome_options=chrome_options)
        # chrome.get("https://google.com")


        # http://stackoverflow.com/questions/31062789/how-to-load-default-profile-in-chrome-using-python-selenium-webdriver
        # from selenium import webdriver
        # from selenium.webdriver.chrome.options import Options
        #
        # options = webdriver.ChromeOptions()
        # options.add_argument("user-data-dir=C:\\Path")  # Path to your chrome profile
        # w = webdriver.Chrome(executable_path="C:\\Users\\chromedriver.exe", chrome_options=options)


        # http://stackoverflow.com/questions/12698843/how-do-i-pass-options-to-the-selenium-chrome-driver-using-python
        # from selenium import webdriver
        # from selenium.webdriver.chrome.options import Options
        # chrome_options = Options()
        # chrome_options.add_argument("--disable-extensions")
        # driver = webdriver.Chrome(chrome_options=chrome_options)

        # mobile_emulation = {"deviceName": "Google Nexus 5"}

        chrome_options = webdriver.ChromeOptions()

        # profile_path = '/home/eyalev/.config/google-chrome/Profile\ 10'
        profile_path = '/home/eyalev/.config/google-chrome'

        # chrome_options.add_argument('--user-data-dir={profile_path}'.format(profile_path=profile_path))
        chrome_options.add_argument('user-data-dir={profile_path}'.format(profile_path=profile_path))

        # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # browser = Browser('chrome', options=chrome_options)

        # import ipdb; ipdb.set_trace()
        # self.browser = splinter.Browser('chrome', options=chrome_options)
        self.browser = splinter.Browser('chrome')

        # from selenium.webdriver.chrome.options import Options
        # chrome_options = Options()
        # chrome_options.add_argument('user-data-dir={profile_path}'.format(profile_path=profile_path))
        # chrome = webdriver.Chrome('chromedriver', chrome_options=chrome_options)
        # chrome.get("https://google.com")

        self.wait_time_in_seconds = wait_time

    def start_browser(self):

        # if EnvUtil().codeship():
        #     sleep(2)

        pass
        # self.browser = splinter.Browser('chrome')
        # self.browser = Browser('firefox')

        # if EnvUtil().codeship():
        #     sleep(2)

    def url(self):

        return self.browser.url

    def visit(self, url):

        self.browser.visit(url)

    def open(self, url):
        return self.visit(url)

    def assert_text(self, text):

        text_present = False

        # for index in xrange(self.wait_time_in_seconds):
        for index in six.moves.range(self.wait_time_in_seconds):

            try:
                text_present = self.browser.is_text_present(text)

                if text_present:
                    break

                sleep(1)

            except StaleElementReferenceException:
                pass

        TestUtil().assert_true(text_present, message='Assert text: ' + text)

    def fill_form(self, data_dict):

        self.browser.fill_form(data_dict)

    def click_css(self, css, sleep_after_find=0):

        for index in six.moves.range(self.wait_time_in_seconds):
            try:
                element = self.browser.find_by_css(css).first
                if element:
                    sleep(sleep_after_find)
                    element.click()
                    return True

            except ElementDoesNotExist:
                pass

            sleep(1)

        raise ElementDoesNotExist(css)

    def assert_css(self, css):

        css_present = False

        for index in six.moves.range(self.wait_time_in_seconds):

            css_present = self.browser.is_element_present_by_css(css)

            if css_present:
                break

            sleep(1)

        TestUtil().assert_true(css_present, 'CSS assertion failed for ' + css)

    def close_browser(self):

        self.browser.quit()

    def click_submit_button(self):

        element = self.browser.find_by_xpath('//button[@type="submit"]')
        element.click()

    def click_partial_link_path(self, partial_link):

        for index in six.moves.range(self.wait_time_in_seconds):

            try:
                element = self.browser.find_link_by_partial_href(partial_link).first

                if element:
                    element.click()
                    return True

            except ElementNotVisibleException:
                pass

            sleep(1)

        raise ElementNotVisibleException(partial_link)

    def assert_css_not_present(self, css):

        self.browser.is_element_not_present_by_css(css)

    def accept_alert(self):

        sleep(1)  # For Codeship
        alert = self.browser.get_alert()
        alert.accept()

    def find_by_xpath(self, path):
        return self.browser.find_by_xpath(path)

    def find_by_id(self, element_id):
        return self.browser.find_by_id(element_id)

    def find_by_css(self, css):
        return self.browser.find_by_css(css)
