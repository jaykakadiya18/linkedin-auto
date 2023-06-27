# import os
# from win32com.client import Dispatch
# import shutil
# import winreg
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from datetime import datetime
# import time
# from stem import Signal

# chromedriver_path = os.path.abspath("chromedriver.exe")
# Chrome_UserData_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google\\Chrome\\User Data')
# Chrome_profile_path = os.path.abspath("Chrome_Data\\")
# Chrome_Path = None
# Range_browser_open = None

# Chrome_Data_path = os.path.abspath("Chrome_Data\\")

# def find_chrome_path():
#     # Check the default installation path
#     default_path = r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
#     if os.path.isfile(default_path):
#         return default_path

#     default_path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'
#     if os.path.isfile(default_path):
#         return default_path

#     # Check the registry for other installation paths
#     reg_path = r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\App Paths\\chrome.exe'
#     with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_READ) as key:
#         value = winreg.QueryValueEx(key, None)[0]
#         if os.path.isfile(value):
#             return value

#     # Chrome not found
#     return None


# def create_chrome_shortcut(Chrome_Path,no):
#     # Find the Chrome executable path
#     if Chrome_Path is None:
#         Chrome_Path = find_chrome_path()

#     # Create a Chrome profile directory
#     profile_dir = os.path.join(Chrome_profile_path, 'UserProfile_{}'.format(str(no)))
#     if not os.path.exists(profile_dir):
#         os.makedirs(profile_dir)

#     # Copy an existing Preferences file to the profile directory, chrome://version/
#     preferences_file = os.path.join(Chrome_UserData_path, 'Default\\Preferences')
#     if not os.path.exists(preferences_file):
#         preferences_file = os.path.join(Chrome_UserData_path, 'Guest Profile\\Preferences')
#     new_preferences_file = os.path.join(profile_dir, 'Preferences')
#     shutil.copy(preferences_file, new_preferences_file)

#     # Create the shortcut
#     shortcut_path = os.path.join(Chrome_profile_path, f"ChromeShortCut_{str(no)}.lnk")

#     # Check if the shortcut file exists
#     if not os.path.exists(shortcut_path):
#         # Create the shortcut
#         import pythoncom

#         # Call CoInitialize
#         pythoncom.CoInitialize()

#         # Your code that uses COM components goes here...
#         shell = Dispatch('WScript.Shell')
#         shortcut = shell.CreateShortCut(shortcut_path)
#         shortcut.TargetPath = Chrome_Path
#         shortcut.Arguments = "--user-data-dir=\"" + profile_dir + "\""
#         shortcut.save()

#         # Call CoUninitialize when you're finished with the COM components
#         pythoncom.CoUninitialize()

#     # Launch the shortcut
#     # os.startfile(shortcut_path)

#     return Chrome_Path


# def connect_driver(no):
#     try:
#         profile_path = os.path.join(Chrome_profile_path, 'UserProfile_{}'.format(str(no)))

#         options = webdriver.ChromeOptions()
#         options.add_argument("start-maximized")
#         # options.add_experimental_option("excludeSwitches", ["enable-automation"])
#         # options.add_experimental_option('useAutomationExtension', False)
#         # options.add_experimental_option("debuggerAddress", f"localhost:{port}")
#         options.add_argument('--disable-notifications')
#         options.add_argument('--disable-geolocation')
#         options.add_argument("--disable-features=WebUSB")
#         options.add_argument("--disable-extensions")
#         options.add_argument("--disable-popup-blocking")
        
#         options.add_argument(
#             'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36')
#         options.add_argument(
#             'Accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
#         options.add_argument('Accept-Language=en-US,en;q=0.5')
#         options.add_argument('Connection=keep-alive')
#         options.add_argument('Upgrade-Insecure-Requests=1')
#         options.add_argument('Sec-Fetch-Dest=document')
#         options.add_argument('Sec-Fetch-Mode=navigate')
#         options.add_argument('Sec-Fetch-Site=none')
#         options.add_argument('Sec-Fetch-User=?1')
#         options.add_argument('Pragma=no-cache')
#         options.add_argument('Cache-Control=no-cache')
        

#         options.add_argument("user-data-dir=" + profile_path)  # Path to your chrome profile
        
#         ser = Service(chromedriver_path)
#         driver = webdriver.Chrome(service=ser, options=options)
#         wait = WebDriverWait(driver, 10)

#         return driver

#     except Exception as e:
#         print(e)
#         pass

# create_chrome_shortcut(Chrome_Path=Chrome_Path, no=1)
# browser = connect_driver(1)
# # browser.get("https://www.linkedin.com/events/gibsonreports-virtualrssevent-p6756991161354784768/")
# time.sleep(1)

import asyncio
from pyppeteer import launch
from time import sleep


async def invite_connections_to_event(event_url):
    browser = await launch(executablePath='C:\Program Files\Google\Chrome\Application\chrome.exe', headless=False)
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 1080})
    
    # Sign in to LinkedIn
    await page.goto('https://www.linkedin.com/login')
    await page.waitForSelector('#username')
    await page.type('#username', '*********')  # Replace with your LinkedIn email
    sleep(1)
    await page.type('#password', '***********')  # Replace with your LinkedIn password
    sleep(1)
    await page.click('button[type="submit"]')
    await page.waitForNavigation()
    sleep(2)
    # Navigate to the event page
    await page.goto(event_url)
    await page.waitForSelector('#ember41')

    # Click the "Invite" button
    await page.click('button[data-control-name="invite_attendees"]')
    # await page.waitForSelector('#ember41')
    sleep(5)
    # Select and invite the top 10 members
    # invitee_selectors = await page.querySelectorAll('ember-checkbox ember-view')

    # invitee_selectors = await page.querySelectorAll('.invite-modal .invitee .entity-result__title-text')

    scroll_height = await page.evaluate('() => document.documentElement.scrollHeight')
    viewport_height = await page.evaluate('() => window.innerHeight')

    while True:
        # Scroll to the bottom of the page
        await page.evaluate('window.scrollTo(0, document.documentElement.scrollHeight)')

        # Wait for a brief moment to allow content to load
        await asyncio.sleep(1)

        # Calculate the new scroll height after scrolling
        new_scroll_height = await page.evaluate('() => document.documentElement.scrollHeight')

        # Break the loop if the scroll height remains the same
        if new_scroll_height == scroll_height:
            break
        scroll_height = new_scroll_height

    for invitee_selector in range(1,11):
        invitee_container = await page.xpath(f'/html/body/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/ul/li[{invitee_selector}]')
        print(invitee_container)
        sleep(0.5)
        if invitee_container:
            invitee_checkbox = await invitee_container[0].querySelector('input[type="checkbox"]')
            if invitee_checkbox:
                await invitee_checkbox.click()

    sleep(2)
    invite = await page.xpath("/html/body/div[3]/div/div/div[2]/div/div[2]/div/button")
    print(invite)
    sleep(1)
    await invite[0].click()
    sleep(2)
    # Close the invite dialog
    try:
        await page.click('.artdeco-modal .artdeco-modal__dismiss')
    except:
        pass
    # Keep the browser open (comment out the next line if you want to close the browser)
    await page.waitForNavigation()

    # Close the browser
    await browser.close()

# Usage example
event_url = 'https://www.linkedin.com/events/gibsonreports-virtualrssevent-p6756991161354784768/'
asyncio.get_event_loop().run_until_complete(invite_connections_to_event(event_url))
