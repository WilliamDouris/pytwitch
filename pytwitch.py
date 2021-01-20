from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

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

        # TODO : May add verification of url or page to make sure we are on channel page

        if not self.is_page_exist():
            print("get_channel_status() - The channel name don't exist")
            return 0

        try:
            if twitch_obj.browser.find_element_by_class_name("tw-strong tw-upcase tw-white-space-nowrap").text is "LIVE": # Overkill, I think we don't need that
                return 0
        except NoSuchElementException:
            return 1

    def is_page_exist(self):
        try:
            self.browser.find_element_by_class_name("core-error__message-container tw-flex tw-flex-column")
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
        pass

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
    twitch_obj = twitch()
    twitch_obj.watch_channel("skyyart")
    print()
