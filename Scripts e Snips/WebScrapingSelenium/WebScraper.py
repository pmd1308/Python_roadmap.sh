import json 
import pyperclip
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class WebScraper:
    def __init__(self, chrome_driver_path, headless=True):
        self.chrome_driver_path = chrome_driver_path
        self.headless = headless
        self.driver = self._initialize_driver()

    def _initialize_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        service = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
        return driver
    
    def save_cookies_to_file(self, file_path):
        cookies = self.driver.get_cookies()
        with open(file_path, 'w') as file:
            json.dump(cookies, file, indent=4)
        print(f"Cookies saved to {file_path}")

    def extract_data(self, tag_name):
        try:
            elements = self.driver.find_elements(By.TAG_NAME, tag_name)
            if not elements:
                raise NoSuchElementException(f"Could not find elements with tag '{tag_name}' on the page.")
            data = [element.text for element in elements]
            return data
        except NoSuchElementException as e:
            print(f"Could not find elements with tag '{tag_name}' on the page.")
            print(e)
            return []
        except Exception as e:
            print("Error extracting data: '{e}'.")
            return []
        
    def wait_for_element(self, wait_type, wait_for):
        wait = WebDriverWait(self.driver, 10)
        if wait_type == 'id':
            wait.until(EC.presence_of_element_located((By.ID, wait_for)))
        elif wait_type == 'name':
            wait.until(EC.presence_of_element_located((By.NAME, wait_for)))
        elif wait_type == 'xpath':
            wait.until(EC.presence_of_element_located((By.XPATH, wait_for)))
        elif wait_type == 'tag':
            wait.until(EC.presence_of_element_located((By.TAG_NAME, wait_for)))
        elif wait_type == 'class':
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, wait_for)))
        elif wait_type == 'css':
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, wait_for)))

    def scrap(self, url,  tag_name, cookie_file, wait_for, wait_type):
        if not validators.url(url):
            print(f"Invalid URL: '{url}'")
            return
        
        try:
            self.driver.get(url)
            self.wait_for_element(wait_type, wait_for)
            print("Successfully scraped")

            self.save_cookies_to_file(cookie_file)
            data = self.extract_data(tag_name)
            if data:
                extracted_text = "\n".join(data)
                pyperclip.copy(extracted_text)
                print(f"Successfully extracted data and copied to clipboard.")
        except TimeoutException:
            print("Error: Page load timed out.")
        except NoSuchElementException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.driver.quit()
            print("Browser closed successfully.")
    