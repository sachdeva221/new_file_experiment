import time

from selenium.webdriver.common.by import By

from new_file_experiment.Base import Base


class Test_maincode(Base):
    def test_initialcode(self):
        self.Driver.find_element(By.ID, "search-input").click()
        self.Driver.find_element(By.NAME, 'search_query').send_keys("python basic")
        self.Driver.find_element(By.CSS_SELECTOR, 'button[class="style-scope ytd-searchbox"]').click()
        time.sleep(2)

        # while(True):
        for i in range(5):
            time.sleep(1)
            self.Driver.execute_script("window.scrollBy(0, 1000)", "")





