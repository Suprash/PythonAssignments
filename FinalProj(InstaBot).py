#First i would want to enter an account. 
#Then i would want to have some followers like ronb naturally
#Then i would also want to have auto reply with "by by". 
#Then I would also want to like the post of ronb if it is not liked without scrolling.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import sys

# Basic Informations
USERNAME = "coding_Everywhere00"
PASSWORD = "W/E5rv9gkD%gPGy"
TARGET_ACCOUNT = "routineofnepalbanda"  # Account to follow and like
AUTO_REPLY_TEXT = "by by"

# chrome driver.
service = Service(r"C:\Users\Suprash\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()  # Helps avoid element visibility issues

# This humanizes the process with random delays.
def human_delay(min_sec=1, max_sec=3):
    time.sleep(random.uniform(min_sec, max_sec))

def login(driver, username, password):
    try:
        print("Attempting to login...")
        driver.get("https://www.instagram.com/accounts/login/")
        
        # Wait untill the programs sees the elements with username.
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "password")
        
        username_input.send_keys(username)
        human_delay(0.5, 1)  # Typing delay
        password_input.send_keys(password)
        human_delay(0.5, 1)  # Typing delay
        password_input.send_keys(Keys.RETURN)
        
        #A problem with login prompt was seens:
        # Handle two possible scenarios:
        # 1. "Save login info" prompt
        # 2. "Turn on notifications" prompt
        
        # First try to find and dismiss "Save login info"
        try:
            not_now_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Not Now') and contains(text(), 'info')]"))
            )
            not_now_button.click()
            print("Dismissed 'Save login info' prompt")
            human_delay()
        except:
            pass
            
        # Then try to find and dismiss notifications prompt
        try:
            not_now_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Not Now') and not(contains(text(), 'info'))]"))
            )
            not_now_button.click()
            print("Dismissed notifications prompt")
            human_delay()
        except:
            pass
            
        # Final verification - check if we're on the main feed
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Home') or contains(text(), 'Search')]"))
        )
        print("Login successful!")
        return True
        
    except Exception as e:
        print(f"Login failed: {str(e)}")
        # Check if there's a "Try Again" button (wrong credentials)
        try:
            if driver.find_element(By.XPATH, "//button[contains(., 'Try Again')]"):
                print("Error: Wrong username or password")
        except:
            pass
        return False

def follow_account(driver, target_username):
    try:
        print(f"Attempting to follow {target_username}...")
        
        # Search for the account
        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Search']/.."))
        )
        search_button.click()
        human_delay()
        
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_input.send_keys(target_username)
        human_delay(1, 2)
        
        # Wait for results and click on the profile
        profile_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '/{target_username}/')]"))
        )
        profile_result.click()
        human_delay(2, 3)
        
        # Wait for profile to load and click follow
        follow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Follow')]/.."))
        )
        if follow_button.text.upper() == "FOLLOW":
            follow_button.click()
            print(f"Successfully followed {target_username}")
            human_delay()
            return True
        else:
            print(f"Already following {target_username}")
            return False
            
    except Exception as e:
        print(f"Failed to follow account: {str(e)}")
        return False

def like_recent_posts(driver, target_username, num_posts=3):
    try:
        print(f"Attempting to like {num_posts} recent posts from {target_username}...")
        
        # Navigate to profile
        driver.get(f"https://www.instagram.com/{target_username}/")
        human_delay(2, 3)
        
        # Get recent posts (first row only - no scrolling)
        posts = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//article//a[contains(@href, '/p/')]"))
        )[:num_posts]
        
        liked_count = 0
        for i, post in enumerate(posts):
            post_url = post.get_attribute("href")
            print(f"Checking post {i+1}: {post_url}")
            
            driver.get(post_url)
            human_delay(2, 3)
            
            # Check if already liked (look for filled heart)
            like_buttons = driver.find_elements(By.XPATH, "//*[local-name()='svg' and @aria-label='Like']")
            if like_buttons:
                like_buttons[0].click()
                print(f"Liked post {i+1}")
                liked_count += 1
            else:
                print(f"Post {i+1} already liked")
            
            human_delay(1, 2)
        
        print(f"Successfully liked {liked_count} posts")
        return True
        
    except Exception as e:
        print(f"Failed to like posts: {str(e)}")
        return False

def auto_reply_to_messages(driver, reply_text="by by"):
    try:
        print("Checking for new messages to reply...")
        
        # Go to DMs
        dm_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'direct/inbox')]"))
        )
        dm_button.click()
        human_delay(3, 4)
        
        # Get unread messages - NEW IMPROVED SELECTOR
        unread_chats = driver.find_elements(By.XPATH, 
            "//div[contains(@aria-label, 'unread') or .//*[contains(@aria-label, 'unread')]] | "
            "//div[contains(@class, 'unread')] | "
            "//div[.//*[contains(@aria-label, 'message')] and .//span[contains(@class, 'count')]]"
        )
        
        if not unread_chats:
            print("No unread messages found")
            return True
        
        replied_count = 0
        for chat in unread_chats[:3]:  # Limit to 3 chats to avoid spamming
            try:
                chat.click()
                human_delay(2, 3)
                
                # Find message input and send reply
                message_input = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "//div[@role='textbox'] | //textarea[@placeholder='Message...']"))
                )
                message_input.send_keys(reply_text)
                human_delay(0.5, 1)  # Typing delay
                message_input.send_keys(Keys.RETURN)
                
                print(f"Replied to a message with '{reply_text}'")
                replied_count += 1
                human_delay(1, 2)
                
            except Exception as e:
                print(f"Failed to reply to one chat: {str(e)}")
                continue
        
        print(f"Replied to {replied_count} messages")
        return True
        
    except Exception as e:
        print(f"Failed to check messages: {str(e)}")
        return False

# Main execution
try:
    # Step 1: Login
    if not login(driver, USERNAME, PASSWORD):
        print("Cannot proceed without login")
        sys.exit(1)
    
    # Dismiss notifications popup if present
    try:
        not_now_button = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'Not Now')]"))
        )
        not_now_button.click()
        human_delay()
    except:
        pass
    
    # Step 2: Follow target account
    follow_account(driver, TARGET_ACCOUNT)
    
    # Step 3: Like recent posts
    like_recent_posts(driver, TARGET_ACCOUNT, num_posts=3)
    
    # Step 4: Auto-reply to messages
    auto_reply_to_messages(driver, AUTO_REPLY_TEXT)
    
    print("All tasks completed successfully!")
    
except Exception as e:
    print(f"An error occurred during execution: {str(e)}")
    
finally:
    # Clean up
    input("Press Enter to close the browser...")
    driver.quit()