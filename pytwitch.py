from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

class pytwitch:
    browser = None
    headless = False

    def __init__(self):
        browser_options = Options()
        browser_options.headless = self.headless
        browser_options.add_argument("--lang=en")

        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        self.browser.get('https://www.twitch.com/')
        pass

    # ---------------------------- Twitch function ---------------------------------------

    def watch_channel(self, str_channel):
        # No need to worry about CAPS and space
        self.browser.get('https://www.twitch.com/' + str_channel)

        if self.get_channel_status() is not "live":
            print("watch_channel() - Channel not on live")
            return 0

        return 1

    def connect_to_twitch(self):
        pass

    def get_channel_status(self, str_channel=None):

        if str_channel is not None:
            self.browser.get('https://www.twitch.com/' + str_channel)

        if not self.is_page_exist():
            raise ValueError("The channel don't exist")

        if self.is_live():
            print("is live")
            return 1
        else:
            print("is not live")
            return 0

    def is_live(self):
        try:
            #self.browser.find_element_by_class_name("live-indicator-container tw-border-radius-large tw-inline")
            self.browser.find_element_by_xpath("//p[@class='live-indicator-container tw-border-radius-large tw-inline']")
            return 1
        except NoSuchElementException:
            return 0

    def is_page_exist(self):
        try:
            self.browser.find_element_by_xpath("//p[@data-a-target='core-error-message']")
            return 0
        except NoSuchElementException:
            return 1

    # ---------------------------- Menu function ---------------------------------------

    def get_following(self, window="live"):  # live, videos, hosts, categories, channels
        pass

    def get_categories(self, window="categories"):  # categories or live channels
        pass

    def get_live_channel(self, game="League of Legends", window="live"):  # live, videos, clips
        pass

    # ---------------------------- Channel function ---------------------------------------

    def farm_channel_token(self):
        pass

    def write_chat(self, message):
        chat_input = self.browser.find_element_by_xpath("//textarea[@data-a-target='chat-input']")
        chat_input.send_keys(message)

    def get_chat(self, contain=None, not_contain=None):
        pass

    def get_info(self):
        # get title
        # get game
        # tag
        # follow
        # notification
        # subscribe
        # viewer
        # time
        # share
        # report
        pass


if __name__ == "__main__":
    twitch_obj = pytwitch()
    twitch_obj.watch_channel("skyyart")
    time.sleep(5)
    try:
        twitch_obj.browser.find_element_by_xpath("//p[@class='live-indicator-container tw-border-radius-large tw-inline']")
        print('ok')
    except:
        pass
    print("let's go ")
    twitch_obj.browser.find_element_by_class_name("tw-strong tw-upcase tw-white-space-nowrap")
