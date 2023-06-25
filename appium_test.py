# from appium import webdriver
# from time import sleep

# desired_caps = {
#     # "platformName": "Android",
#     # "deviceName": "Pixel 6 API 31",
#     # "appPackage": "com.linkedin.android",
#     # "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
#     # "noReset": True,
#     # "idleTimeout": 60000,
#     # "adbExecTimeout": 120000,
#     # "newCommandTimeout": 3000,
#     # "automationName": "UiAutomator2"
#     "platformName": "Android",
#     "deviceName": "Pixel_6_API_30",  # Replace with your emulator device name
#     "appPackage": "com.linkedin.android",
#     "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
#     "noReset": True,
#     "automationName": "UiAutomator2"
# }

# driver = webdriver.Remote('http://localhost:4723', desired_caps)

# # Wait for the app to load
# sleep(10)

# # Click the "Sign In" button
# # sign_in_button = driver.find_element_by_id('com.linkedin.android:id/growth_prereg_fragment_sign_in_button')
# # sign_in_button.click()

# # # Enter your login credentials
# # username_field = driver.find_element_by_id('com.linkedin.android:id/growth_login_join_fragment_username')
# # username_field.send_keys('jp738317@gmail.com')

# # password_field = driver.find_element_by_id('com.linkedin.android:id/growth_login_join_fragment_password')
# # password_field.send_keys('liJay@27')

# # Click the "Sign In" button
# login_button = driver.find_element_by_id('com.linkedin.android:id/growth_login_fragment_sign_in')
# login_button.click()

# # Perform additional actions or assertions as needed

# # Close the driver session
# driver.quit()



from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from time import sleep

# Set the desired capabilities
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",  # Replace with your emulator device name
    "appPackage": "com.linkedin.android",
    "appActivity": "com.linkedin.android.authenticator.LaunchActivity",
    "noReset": True,
    "automationName": "UiAutomator2",
    "mobile:deepLink": "linkedin://profile/vimal-navadiya-549889215/"
}

# Initialize the Appium driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# # Retrieve battery related information
# battery_info = driver.execute_script('mobile: batteryInfo')

# # Print battery information
# print("Battery Level:", battery_info['level'])
# print("Battery State:", battery_info['state'])
# print("Is Charging:", battery_info['isCharging'])

# # Close the driver
# driver.quit()



# Wait for the LinkedIn app to load
sleep(5)

# Open a LinkedIn profile using a deep link
# driver.get("linkedin://profile/vimal-navadiya-549889215/")  # Replace "profileID" with the actual LinkedIn profile ID
print("done")
# Wait for the profile to load
sleep(5)

# Click on "Personalize Invite" button
# personalize_invite_button = driver.find_element("//button[contains(text(),'Personalize Invite')]")
# personalize_invite_button.click()

# # Type a connect message
# connect_message_input = driver.find_element_by_xpath("//textarea[@placeholder='Say hi to connect']")
# connect_message_input.send_keys("Hello, I would like to connect with you!")

# # Click on the "Send Invitation" button
# send_invitation_button = driver.find_element_by_xpath("//button[contains(text(),'Send invitation')]")
# send_invitation_button.click()

# # Close the driver
# driver.quit()