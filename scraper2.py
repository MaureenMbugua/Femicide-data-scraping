# Import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import csv

# Initialize Chrome browser instance
driver = webdriver.Chrome()

# URL of the target femicide database page
website = 'https://www.africadatahub.org/femicide-kenya-database'
driver.get(website)

#Scroll until all cards have loaded
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)  # Give time for cards to load

    # Compare new height with previous height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break  # No more new content to load
    last_height = new_height

# Implicit wait to allow page elements to load and cookie popup to appear
driver.implicitly_wait(5)

# Close the cookie popup modal by clicking the close button
driver.find_element(By.XPATH, "//a[@id='close-modal2']").click()
time.sleep(3) # Extra wait to ensure modal closes and sites loads fully before proceeding

# Locate the container that holds all femicide cards
list_all = driver.find_element(By.CSS_SELECTOR, '#w-node-_33992fe6-30af-b0d1-21dc-3bff5128b970-2fedcb60')

# Get a list of individual card elements
list_each = list_all.find_elements(By.CSS_SELECTOR, "div[class='collection-item-7 w-dyn-item']")

# Create the CSV file and write header
with open('femicide_data.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Initialize counter
    counter = 0
    # Loop through each card and extract data
    for list_item in list_each[-1:-12:-1]:
        
        # Counter to track progress
        counter+=1
        print(f'[{counter}/{len(list_each)}] Extracting data....')

        # Locate and click the button to open the popup modal  
        pop_up_button = list_item.find_element(By.CSS_SELECTOR, "div.fs_modal_femicide_show")
        pop_up_button.click()
        driver.implicitly_wait(10) # Allow time for modal contents to be available
        
        # Get the modal content once it's opened
        pop_content = list_item.find_element(By.CSS_SELECTOR, "div[role='dialog']")
        
        # Extract and store Name
        name = pop_content.find_element(By.CSS_SELECTOR, "div[fs-cmsfilter-field='Name']").text
        
        # Extract and store other victim details based on order
        details = pop_content.find_elements(By.CSS_SELECTOR, "div[class='text-block-47']")
        age = details[0].text
        location = details[1].text
        date = details[2].text
        suspect = details[3].text
        verdict_time = details[4].text
        
        # Extract and store the source URL
        source = pop_content.find_element(By.TAG_NAME, "a").get_attribute("href")

        # Write to CSV immediately
        writer.writerow([name, age, location, date, suspect, verdict_time, source])

        time.sleep(0.5) # Pause before closing the modal

        # Find the close button 
        close_button = pop_content.find_element(By.XPATH, "//div[@aria-label='Close modal']")
        # Click using JavaScript to avoid interaction issues
        driver.execute_script("arguments[0].click();", close_button)

        # Wait until the modal becomes invisible before proceeding
        WebDriverWait(driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[role='dialog']")))

        # Print the extracted data for this entry
        print(f'Name: {name} | Age: {age} | Location: {location} | Date: {date} | Suspect: {suspect} | Verdict_time: {verdict_time} | Source_url: {source}')
        
        time.sleep(1) # Wait before moving to the next card

# Close Chrome driver session
driver.quit()