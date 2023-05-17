import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from new_file_experiment.Base import Base


class Test_maincode(Base):
    def test_initialcode(self):
        self.Driver.find_element(By.ID, "search-input").click()
        self.Driver.find_element(By.NAME, 'search_query').send_keys("python basic")
        self.Driver.find_element(By.CSS_SELECTOR, 'button[class="style-scope ytd-searchbox"]').click()
        time.sleep(2)

        # # while(True):
        # for i in range(5):
        #     time.sleep(1)
        #     self.Driver.execute_script("window.scrollBy(0, 1000)", "")

        self.Driver.execute_script("window.scrollBy(0, 1000)", "")

        Action = ActionChains(self.Driver)

        # Action.move_to_element(self.Driver.find_element(By.XPATH, '(//div[@class="style-scope ytd-video-renderer"])[1]')).perform()
        List = self.Driver.find_elements(By.XPATH, '(//div[@class="style-scope ytd-item-section-renderer"])[15]/ytd-video-renderer')
        for i in List:
            Action.move_to_element(i[5]).perform()



