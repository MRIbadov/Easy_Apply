from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set your LinkedIn account credentials
ACCOUNT_EMAIL = 'gmail@gmail.com'
ACCOUNT_PASSWORD = 'password'
PHONE = '511200100'

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
# Uncomment the following line if you want to run in headless mode
# chrome_options.add_argument('--headless')

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Navigate to the LinkedIn job search page
driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&keywords=product%20Analyst&location=taiwan&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0')

# Wait for page to load (you may need to adjust the sleep duration)
time.sleep(2)

# Find and click the "Sign in" button
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

# Wait for the login page to load (you may need to adjust the sleep duration)
time.sleep(5)

# Enter the email and password and submit the form
email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# Initialize page number
page = 2

while page < 5:
    i = 0

    # Loop to scroll down and load more job listings
    while i < 4:
        jobs_list = driver.find_elements_by_css_selector(".job-card-container--clickable")
        print(len(jobs_list))
        driver.execute_script("arguments[0].scrollIntoView();", jobs_list[-1])
        time.sleep(2)
        i += 1

    for listing in jobs_list:
        listing.click()
        print("called")

        time.sleep(3)

        try:
            apply_button = driver.find_element_by_css_selector(".jobs-apply-button--top-card")

            if apply_button.text == 'Easy Apply':
                apply_button.click()
                time.sleep(5)
                submit_button = driver.find_element_by_class_name("artdeco-button--primary")

                # Check the text of the submit button
                if submit_button.text == 'Next':
                    time.sleep(5)
                    submit_button.click()
                    resume_button = driver.find_element_by_css_selector("[aria-label='Choose Resume']")
                    resume_button.click()
                    time.sleep(3)
                    review_button = driver.find_element_by_class_name("artdeco-button--primary")

                    if review_button.text == 'Review':
                        print('Review section')
                        review_button.click()
                        time.sleep(3)
                        fin_button = driver.find_element_by_css_selector("[aria-label='Submit application']")
                        fin_button.click()
                        time.sleep(3)
                    else:
                        print('Continue section')
                        review_button.click()
                        time.sleep(5)

                        qCheck = driver.find_element_by_class_name("t-16")

                        if qCheck.text == 'Additional Questions':
                            time.sleep(3)
                            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                            close_button.click()
                            time.sleep(5)

                            save_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                            save_button.click()
                            time.sleep(5)
                        else:
                            next_button = driver.find_element_by_css_selector("[aria-label='Review your application']")
                            next_button.click()
                            time.sleep(3)
                            fin_button = driver.find_element_by_css_selector("[aria-label='Submit application']")
                            fin_button.click()
                            time.sleep(3)

                elif submit_button.text == 'Submit application':
                    resume_button = driver.find_element_by_css_selector("[aria-label='Choose Resume']")
                    resume_button.click()
                    submit_button.click()
                    time.sleep(3)
                else:
                    close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
                    close_button.click()
                    time.sleep(5)

                try:
                    check_close_btn = driver.find_element_by_class_name("artdeco-modal__dismiss")
                    check_close_btn.click()
                    try:
                        time.sleep(5)
                        save_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                        save_button.click()
                    except:
                        pass
                except NoSuchElementException:
                    pass

            except NoSuchElementException:
                print("No application button, skipped.")
                try:
                    check_close_btn = driver.find_element_by_class_name("artdeco-modal__dismiss")
                    check_close_btn.click()
                    try:
                        time.sleep(5)
                        save_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
                        save_button.click()
                    except:
                        pass
                except NoSuchElementException:
                    pass
                continue

    # Click the next page button
    driver.find_elements_by_xpath(f"//button[@aria-label='Page {page}']")[0].click()
    page += 1

# Wait before quitting the browser
time.sleep(5)
driver.quit()
