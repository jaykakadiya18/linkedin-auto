# from flask import (flash, Flask, render_template, request, session, redirect, url_for)
# import subprocess
# import os
# from win32com.client import Dispatch
# import shutil
# import winreg
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.remote.webelement import WebElement
# import asyncio
# import json, threading
# import pandas as pd
# import requests
# from requests.exceptions import ProxyError, ReadTimeout, ConnectionError
# import random
# from datetime import datetime
# import time
# import stem
# import stem.process
# import requests
# from stem.control import Controller
# from flaskwebgui import FlaskUI
# from stem import Signal
# import re
# import psutil
# from main import finding_process_main

# # pyinstaller --add-data "templates/*;templates/" --add-data "static/*;static/" app_main_file.py 

# app = Flask(__name__)

# # SqlAlchemy Database Configuration With Mysql
# app.config["SECRET_KEY"] = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
# app.config["given_process"] = "new"
# app.config["given_time"] = "new"

# secure_type = "http"



# # import aiohttp
# # import openpyxl
# # https://mbasic.facebook.com/login/?ref=dbl&fl&login_from_aymh=1

# chromedriver_path = os.path.abspath("chromedriver.exe")
# Chrome_UserData_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Google\\Chrome\\User Data')
# Chrome_profile_path = os.path.abspath("Chrome_Data\\")
# Chrome_Path = None
# Range_browser_open = None


# def kill_process_using_port(port):
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             connections = proc.connections()
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             continue

#         for conn in connections:
#             if conn.laddr.port == port:
#                 pid = proc.pid
#                 print(f"Killing process {pid} ({proc.name()})")
#                 try:
#                     proc.kill()
#                 except:
#                     pass

# def change_tor_exit_node():
#     with Controller.from_port(port=9051) as controller:
#         controller.authenticate()
#         controller.signal(Signal.NEWNYM)


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


# def connect_driver(no, session):
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

        
#         if session["PROXY"] != None:
#             change_tor_exit_node()
#             options.add_argument('--proxy-server=%s' % session["PROXY"])


#         options.add_argument(
#             'user-agent=Mozilla/5.0 (Linux; Android 11; 10011886A Build/RP1A.200720.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Safari/537.36')
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


# def port_fatch():
#     try:
#         port_list = []
#         with open('chrome_data.bat', 'r') as file:
#             lines = file.readlines()
#             for line in lines:
#                 if "port" in str(line):
#                     index1 = str(line).index('port=') + len('port=')
#                     index2 = str(line).index(' ', index1)
#                     port = line[index1:index2]
#                     port_list.append(port)
#         return port_list
#     except Exception as e:
#         print(e)
#         return None


# def create_chrome_file(li):
#     try:
#         # create a list of lines to write
#         filename = os.path.abspath("chor.bat")
#         # open a file for writing
#         with open(filename, 'w') as f:
#             # iterate over the lines and write each line
#             for line in li:
#                 f.write(line + '\n')

#         f.close()

#         return "done"

#     except Exception as e:
#         print(e)
#         return "error"


# def join_group(groups_join, driver):
#     try:
#         if groups_join:
#             for gid in groups_join:
#                 try:
#                     driver.get(f"https://mbasic.facebook.com/groups/{gid}")
#                     time.sleep(5)
#                     driver.find_element(By.XPATH, "//input[@value='Join Group' and @type='submit']").click()
#                     time.sleep(5)
#                 except Exception as e:
#                     continue
#         time.sleep(3)
#     except Exception as e:
#         print(e)
#         pass

# def accepts_requests(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/friends/center/requests/')
#         time.sleep(3)

#         seemore_element = None
#         perent_seemore_element = None
        
#         try:
#             seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#             perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#         except:
#             pass

#         if seemore_element!=None and perent_seemore_element!=None:
#             while seemore_element!=None and perent_seemore_element!=None:
#                 ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Confirm']")
#                 for ul_element in ul_elements:
#                     perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                     url = perent_element.get_attribute("href")
#                     driver.execute_script(f"window.open('{url}', '_blank')")
#                     driver.switch_to.window(driver.window_handles[1])
#                     time.sleep(3)
#                     try:
#                         driver.close()  # close the new tab
#                         driver.switch_to.window(driver.window_handles[0])
#                     except:
#                         pass                        
                    
#                 perent_seemore_element.click()
                        
#                 try:
#                     seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#                     perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#                 except:
#                     seemore_element = None
#                     perent_seemore_element = None

#         else:
#             ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Confirm']")
#             for ul_element in ul_elements:
#                 perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                 url = perent_element.get_attribute("href")
#                 driver.execute_script(f"window.open('{url}', '_blank')")
#                 driver.switch_to.window(driver.window_handles[1])
#                 time.sleep(3)
#                 try:
#                     driver.close()  # close the new tab
#                     driver.switch_to.window(driver.window_handles[0])
#                 except:
#                     pass          


#         time.sleep(3)

#     except Exception as e:
#         pass

# def schedual_sharing_fun():

#     while True:
#         try:
#             di = {"join_group": "3", "leave_group": "4", "like_post": "5", "like_group_post": "6", "sharing_post": "7", "comments_feed": "8",
#                 "accept_requests": "13", "send_requests": "14", "delete_requests": "15"}
#             get_time = get_current_time()
#             given_time = app.config["given_time"]
#             given_response = app.config["given_process"]

#             if given_time!="new" and given_response!="new":
#                 given_time1 = given_time.replace("T", " ")
#                 dt1 = datetime.strptime(get_time, "%Y-%m-%d %H:%M")
#                 dt2 = datetime.strptime(given_time1, "%Y-%m-%d %H:%M")
#                 count = 0
#                 if dt1 == dt2 and count==0:
#                     res_main = finding_process_main("2")
#                     res_main = finding_process_main("9")
#                     res_main = finding_process_main(di[given_response.lower()])
#                     count+=1
#                     app.config["given_time"] = "new"
#                     app.config["given_process"] = "new"

#         except Exception as e:
#             print(e)
            


# def send_requests(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/friends/')
#         time.sleep(3)

#         seemore_element = None
#         perent_seemore_element = None
        
#         try:
#             seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#             perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#         except:
#             pass

#         if seemore_element!=None and perent_seemore_element!=None:
#             while seemore_element!=None and perent_seemore_element!=None:
#                 ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Add Friend']")
#                 for ul_element in ul_elements:
#                     perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                     url = perent_element.get_attribute("href")
#                     driver.execute_script(f"window.open('{url}', '_blank')")
#                     driver.switch_to.window(driver.window_handles[1])
#                     time.sleep(3)
#                     try:
#                         driver.close()  # close the new tab
#                         driver.switch_to.window(driver.window_handles[0])
#                     except:
#                         pass
#                 perent_seemore_element.click()
                        
#                 try:
#                     seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#                     perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#                 except:
#                     seemore_element = None
#                     perent_seemore_element = None

#         else:
#             ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Add Friend']")
#             for ul_element in ul_elements:
#                 perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                 url = perent_element.get_attribute("href")
#                 driver.execute_script(f"window.open('{url}', '_blank')")
#                 driver.switch_to.window(driver.window_handles[1])
#                 time.sleep(3)
#                 try:
#                     driver.close()  # close the new tab
#                     driver.switch_to.window(driver.window_handles[0])
#                 except:
#                     pass         


#         time.sleep(3)

#     except Exception as e:
#         pass

# def delete_requests(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/friends/center/requests/')
#         time.sleep(3)

#         seemore_element = None
#         perent_seemore_element = None
        
#         try:
#             seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#             perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#         except:
#             pass

#         if seemore_element!=None and perent_seemore_element!=None:
#             while seemore_element!=None and perent_seemore_element!=None:
#                 ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Delete request']")
#                 for ul_element in ul_elements:
#                     perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                     url = perent_element.get_attribute("href")
#                     driver.execute_script(f"window.open('{url}', '_blank')")
#                     driver.switch_to.window(driver.window_handles[1])
#                     time.sleep(3)
#                     try:
#                         driver.close()  # close the new tab
#                         driver.switch_to.window(driver.window_handles[0])
#                     except:
#                         pass                        
                    
#                 perent_seemore_element.click()
                        
#                 try:
#                     seemore_element = driver.find_element(by=By.XPATH, value="//span[text()='See more']")
#                     perent_seemore_element = seemore_element.find_element(by=By.XPATH, value="./..")
#                 except:
#                     seemore_element = None
#                     perent_seemore_element = None

#         else:
#             ul_elements = driver.find_elements(by=By.XPATH, value="//span[text()='Delete request']")
#             for ul_element in ul_elements:
#                 perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#                 url = perent_element.get_attribute("href")
#                 driver.execute_script(f"window.open('{url}', '_blank')")
#                 driver.switch_to.window(driver.window_handles[1])
#                 time.sleep(3)
#                 try:
#                     driver.close()  # close the new tab
#                     driver.switch_to.window(driver.window_handles[0])
#                 except:
#                     pass          


#         time.sleep(3)

#     except Exception as e:
#         pass



# def comments(driver, list_comment):
#     try:
#         driver.get('https://mbasic.facebook.com/')
#         time.sleep(3)

#         a_tags = driver.find_elements(by=By.XPATH, value="//a[text()='Comment']")
#         a_tags = [a_tag.get_attribute("href") for a_tag in a_tags]
#         for url in a_tags:
#             driver.execute_script(f"window.open('{url}', '_blank')")
#             driver.switch_to.window(driver.window_handles[1])
#             # index1 = url.index('ft_ent_identifier=')
#             # index2 = url.index('&', index1)
#             # id = url[index1 + len('ft_ent_identifier='):index2]
#             time.sleep(3)
#             try:
#                 comment_field = driver.find_element(by=By.XPATH, value="//input[@name='comment_text']")
#                 comment_button = driver.find_element(by=By.XPATH, value="//input[@value='Comment']")
#                 comment_field.send_keys(random.choice(list_comment))
#                 comment_button.click()
#                 time.sleep(3)
#             except Exception as e:
#                 time.sleep(1)
#             finally:
#                 driver.close()  # close the new tab
#                 driver.switch_to.window(driver.window_handles[0])

#         time.sleep(3)

#     except Exception as e:
#         pass

# def get_current_time():
#     try:
#         current_time = datetime.now()
#         current_time_str = current_time.strftime("%Y-%m-%d %H:%M")
#         return current_time_str
#     except Exception as e:
#         return ""


# def comment_group_post(driver, list_comment):
#     try:
#         driver.get('https://mbasic.facebook.com/groups/')
#         time.sleep(3)
#         try:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups You Are In']")
#         except:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups you are in']")
#         if ul_element is not None:
#             perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#             a_tags = perent_element.find_elements(By.XPATH, ".//a[@href]")
#             group_link = [a_tag.get_attribute("href") for a_tag in a_tags]
#             for url in group_link:
#                 try:
#                     driver.get(url)
#                     time.sleep(3)
#                     group_id = driver.find_element(By.XPATH, "//meta[@property='al:android:url']")
#                     group_id = group_id.get_attribute("content").replace('fb://group/', '').strip()

#                     a_tags = driver.find_elements(by=By.XPATH, value="//a[text()='Comment']")
#                     a_tags = [a_tag.get_attribute("href") for a_tag in a_tags]
#                     for url in a_tags:
#                         driver.execute_script(f"window.open('{url}', '_blank')")
#                         driver.switch_to.window(driver.window_handles[1])
#                         # index1 = url.index('ft_ent_identifier=')
#                         # index2 = url.index('&', index1)
#                         # id = url[index1 + len('ft_ent_identifier='):index2]
#                         time.sleep(3)
#                         try:
#                             comment_field = driver.find_element(by=By.XPATH, value="//input[@name='comment_text']")
#                             comment_button = driver.find_element(by=By.XPATH, value="//input[@value='Comment']")
#                             comment_field.send_keys(random.choice(list_comment))
#                             comment_button.click()
#                             time.sleep(3)
#                         except Exception as e:
#                             time.sleep(1)
#                         finally:
#                             driver.close()  # close the new tab
#                             driver.switch_to.window(driver.window_handles[0])

#                 except Exception as e:
#                     continue

#         time.sleep(3)

#     except Exception as e:
#         print(e)
#         pass

# def post_data(account_data, driver, i):
#     try:
#         driver.get('https://mbasic.facebook.com/groups/')
#         time.sleep(3)
#         try:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups You Are In']")
#         except:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups you are in']")
#         if ul_element is not None:
#             perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#             a_tags = perent_element.find_elements(By.XPATH, ".//a[@href]")
#             group_link = [a_tag.get_attribute("href") for a_tag in a_tags]
#             for url in group_link:
#                 try:
#                     driver.get(url)
#                     time.sleep(3)
#                     group_id = driver.find_element(By.XPATH, "//meta[@property='al:android:url']")
#                     group_id = group_id.get_attribute("content").replace('fb://group/', '').strip()

#                     # post data on group
#                     post_list = [x.Post for x in account_data if int(x.Account) == i + 1 and x.Group == group_id]

#                     for post_data in post_list:
#                         try:
#                             driver.get(f"https://mbasic.facebook.com/groups/{group_id}")
#                             time.sleep(3)
#                             text_area = driver.find_element(by=By.XPATH, value="//textarea[@name='xc_message']")
#                             text_area.send_keys(post_data)
#                             time.sleep(3)
#                             driver.find_element(by=By.XPATH, value="//input[@name='view_post']").click()
#                             time.sleep(3)
#                         except Exception as e:
#                             continue

#                 except Exception as e:
#                     continue
#         time.sleep(3)

#     except Exception as e:
#         print(e)
#         pass


# def like_post(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/')
#         time.sleep(3)

#         a_tags = driver.find_elements(by=By.XPATH, value="//a[text()='Like']")
#         a_tags = [a_tag.get_attribute("href") for a_tag in a_tags]
#         for url in a_tags:
#             driver.execute_script(f"window.open('{url}', '_blank')")
#             driver.switch_to.window(driver.window_handles[1])
#             index1 = url.index('ft_ent_identifier=')
#             index2 = url.index('&', index1)
#             id = url[index1 + len('ft_ent_identifier='):index2]
#             time.sleep(3)
#             try:
#                 like_parent = driver.find_elements(by=By.XPATH, value=f"//div[@id='actions_{id}']")

#                 like_a = like_parent.find_elements(by=By.XPATH, value="//span[text()='Like']")
#                 perent_element = like_a.find_element(by=By.XPATH, value="./..")
#                 driver.get(perent_element.get_attribute("href"))
#                 time.sleep(3)
#             except Exception as e:
#                 time.sleep(1)
#             finally:
#                 driver.close()  # close the new tab
#                 driver.switch_to.window(driver.window_handles[0])

#         time.sleep(3)

#     except Exception as e:
#         print(e)
#         pass


# def like_group_post(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/groups/')
#         time.sleep(3)
#         try:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups You Are In']")
#         except:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups you are in']")
#         if ul_element is not None:
#             perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#             a_tags = perent_element.find_elements(By.XPATH, ".//a[@href]")
#             group_link = [a_tag.get_attribute("href") for a_tag in a_tags]
#             for url in group_link:
#                 try:
#                     driver.get(url)
#                     time.sleep(3)
#                     group_id = driver.find_element(By.XPATH, "//meta[@property='al:android:url']")
#                     group_id = group_id.get_attribute("content").replace('fb://group/', '').strip()

#                     a_tags = driver.find_elements(by=By.XPATH, value="//a[text()='Like']")
#                     a_tags = [a_tag.get_attribute("href") for a_tag in a_tags]
#                     for url in a_tags:
#                         driver.execute_script(f"window.open('{url}', '_blank')")
#                         driver.switch_to.window(driver.window_handles[1])
#                         index1 = url.index('ft_ent_identifier=')
#                         index2 = url.index('&', index1)
#                         id = url[index1 + len('ft_ent_identifier='):index2]
#                         time.sleep(3)
#                         try:
#                             like_parent = driver.find_elements(by=By.XPATH, value=f"//div[@id='actions_{id}']")

#                             like_a = like_parent.find_elements(by=By.XPATH, value="//span[text()='Like']")
#                             perent_element = like_a.find_element(by=By.XPATH, value="./..")
#                             driver.get(perent_element.get_attribute("href"))
#                             time.sleep(3)
#                         except Exception as e:

#                             try:
#                                 driver.find_elements(by=By.XPATH,
#                                                      value="//*[@id=\"root\"]/table/tbody/tr/td/ul/li[1]/table/tbody/tr/td/a").click()
#                                 time.sleep(3)
#                             except Exception as e:
#                                 time.sleep(1)
#                         finally:
#                             driver.close()  # close the new tab
#                             driver.switch_to.window(driver.window_handles[0])

#                 except Exception as e:
#                     continue

#         time.sleep(3)

#     except Exception as e:
#         print(e)
#         pass


# def leave_group(driver):
#     try:
#         driver.get('https://mbasic.facebook.com/groups/')
#         time.sleep(3)
#         try:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups You Are In']")
#         except:
#             ul_element = driver.find_element(by=By.XPATH, value="//h3[text()='Groups you are in']")

#         if ul_element is not None:
#             perent_element = ul_element.find_element(by=By.XPATH, value="./..")
#             a_tags = perent_element.find_elements(By.XPATH, ".//a[@href]")
#             group_link = [a_tag.get_attribute("href") for a_tag in a_tags]
#             for url in group_link:
#                 try:
#                     driver.get(url)
#                     time.sleep(3)
#                     group_id = driver.find_element(By.XPATH, "//meta[@property='al:android:url']")
#                     group_id = group_id.get_attribute("content").replace('fb://group/', '').strip()
#                     driver.get(f"https://mbasic.facebook.com/group/leave/?group_id={group_id}")
#                     time.sleep(3)
#                     try:
#                         driver.find_element(By.XPATH, "//input[@value='Leave Group']").click()
#                     except:
#                         driver.find_element(By.XPATH, "//input[@value='Leave group']").click()
#                     time.sleep(3)
#                 except Exception as e:
#                     continue
#         time.sleep(3)

#     except Exception as e:
#         print(e)
#         time.sleep(1)


# def run_bat(filename):
#     try:
#         # Replace "path/to/batch/file.bat" with the actual path to your batch file
#         batch_file_path = os.path.abspath(filename)

#         # Run the batch file
#         subprocess.call([batch_file_path])

#     except Exception as e:
#         print(e)
#         pass



# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/", methods=["GET", "POST"])
# def home():
#     """
#     That function was register for new user
#     """
#     try: 
#         PROXY = "socks5://127.0.0.1:9050"
#         session["PROXY"] = PROXY
#         proxy = session.get("PROXY", "")
#         if proxy:
#             SOCKS_PORT = 9050
#             kill_process_using_port(SOCKS_PORT)
#             TOR_PATH = os.path.abspath("Tor_Browser\\Browser\\TorBrowser\\Tor\\tor.exe")

#             tor_process = stem.process.launch_tor_with_config(
#                 config = { 'SocksPort': str(SOCKS_PORT),'ControlPort': '9051','MaxCircuitDirtiness' : '60',},
#             init_msg_handler = lambda line: print(line) if re.search('Bootstrapped', line) else False,
#             tor_cmd = TOR_PATH
#             )
#         else:
#             session["PROXY"]=None
            
#         return render_template("main_facebook.html")

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/create_browser_main", methods=["GET", "POST"])
# def create_browser_main():
#     """
#     That function was register for new user
#     """
#     try:
#         session["Chrome_Path"] = None
#         if request.method=="POST":
#             how_m = request.form["count"]
#             session["create_browser_value"] = how_m
#             how_m = int(how_m)
#             for n in range(0, how_m):
#                 Chrome_Path = create_chrome_shortcut(session["Chrome_Path"], n + 1)
#                 session["Chrome_Path"] = Chrome_Path
#             flash("Browser Create Successfully...........")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("create_browser.html")

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/open_browser_main", methods=["GET", "POST"])
# def open_browser_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             brow_open = request.form["count_value"]
#             Range_browser_open = str(brow_open)
#             session["Range_browser_open"] = Range_browser_open
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 driver = connect_driver(i, session)
#                 name = "driver_"+str(i)
#                 app.config[name]=driver
#             flash("Successfully browser open...........")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("open_browser.html")

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/join_group_main", methods=["GET", "POST"])
# def join_group_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads = []
#             excelsheet_path = os.path.abspath("Facebook_User_Data.xlsx")
#             df = pd.read_excel(excelsheet_path, sheet_name='Sheet1')
#             max_row = df.shape[0]
#             max_column = df.shape[1]



#             class objData:
#                 Account = ''
#                 Group = ''
#                 Post = ''


#             account_data = []

#             for a, b, c in zip(df["Account"], df["Group"], df["Post"]):
#                 obj = objData()

#                 obj.Account = str(a)
#                 obj.Group = str(b)
#                 obj.Post = str(c)

#                 account_data.append(obj)

#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 groups_join = [item.Group for item in account_data if int(item.Account) == int(str(i + 1))]
#                 groups_join = list(set(groups_join))
#                 t2 = threading.Thread(target=join_group, args=(groups_join, driver,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete join group process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))


#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# def login_facebook_fun(driver):
#     try:
#         driver.get("https://mbasic.facebook.com/")
#         time.sleep(3600)

#     except Exception as e:
#         print(e)


# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/login_facebook", methods=["GET", "POST"])
# def login_facebook():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             brow_open = request.form["count_value"]
#             open_browser_name = str(brow_open)
#             start = int(open_browser_name.split('-')[0])
#             end = int(open_browser_name.split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 t2 = threading.Thread(target=login_facebook_fun, args=(driver,))
#                 t2.start()

#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("login_facebook.html")


#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))



# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/leave_group_main", methods=["GET", "POST"])
# def leave_group_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 # driver = connect_driver(i, session)
#                 t2 = threading.Thread(target=leave_group, args=(driver,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete leave group process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/like_post_main", methods=["GET", "POST"])
# def like_post_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             how_m = request.form["count"]
#             threads=[]
#             if how_m == "Feed":
#                 if session["Range_browser_open"] != None:
#                     start = int(session["Range_browser_open"].split('-')[0])
#                     end = int(session["Range_browser_open"].split('-')[1])
#                     for i in range(start, end + 1):
#                         name = "driver_"+str(i)
#                         driver = app.config.get(name, "")
#                         # driver = connect_driver(i, session)
#                         t2 = threading.Thread(target=like_post, args=(driver,))
#                         threads.append(t2)
#                         t2.start()

#                     for t in threads:
#                         t.join()

#                     flash("Successfully complete like post process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#                 else:
#                     flash("Please first run create browser and open broswer process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#             else:
#                 if session["Range_browser_open"] != None:
#                     start = int(session["Range_browser_open"].split('-')[0])
#                     end = int(session["Range_browser_open"].split('-')[1])
#                     for i in range(start, end + 1):
#                         name = "driver_"+str(i)
#                         driver = app.config.get(name, "")
#                         # driver = connect_driver(i, session)
#                         t2 = threading.Thread(target=like_group_post, args=(driver,))
#                         threads.append(t2)
#                         t2.start()

#                     for t in threads:
#                         t.join()

#                     flash("Successfully complete like group post process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#                 else:
#                     flash("Please first run create browser and open broswer process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("like_post.html")


#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/schedual_sharing", methods=["GET", "POST"])
# def schedual_sharing():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             given_time = request.form["meeting"]
#             process_given = request.form["process_pr"]
#             app.config["given_time"] = given_time
#             app.config["given_process"] = process_given
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("schedual_sharing.html")


#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))


# @app.route("/comment_post_main", methods=["GET", "POST"])
# def comment_post_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             how_m = request.form["count"]
#             comment = request.form["comment"]
#             list_comment = comment.split(",")
#             threads=[]
#             if how_m == "Feed":
#                 if session["Range_browser_open"] != None:
#                     start = int(session["Range_browser_open"].split('-')[0])
#                     end = int(session["Range_browser_open"].split('-')[1])
#                     for i in range(start, end + 1):
#                         name = "driver_"+str(i)
#                         driver = app.config.get(name, "")
#                         # driver = connect_driver(i, session)
#                         t2 = threading.Thread(target=comments, args=(driver, list_comment,))
#                         threads.append(t2)
#                         t2.start()

#                     for t in threads:
#                         t.join()

#                     flash("Successfully complete like post process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#                 else:
#                     flash("Please first run create browser and open broswer process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#             else:
#                 if session["Range_browser_open"] != None:
#                     start = int(session["Range_browser_open"].split('-')[0])
#                     end = int(session["Range_browser_open"].split('-')[1])
#                     for i in range(start, end + 1):
#                         name = "driver_"+str(i)
#                         driver = app.config.get(name, "")
#                         # driver = connect_driver(i, session)
#                         t2 = threading.Thread(target=comment_group_post, args=(driver, list_comment,))
#                         threads.append(t2)
#                         t2.start()

#                     for t in threads:
#                         t.join()

#                     flash("Successfully complete like group post process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#                 else:
#                     flash("Please first run create browser and open broswer process")
#                     return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             return render_template("comments_post.html")


#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))



# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/create_post_main", methods=["GET", "POST"])
# def create_post_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             excelsheet_path = os.path.abspath("Facebook_User_Data.xlsx")
#             df = pd.read_excel(excelsheet_path, sheet_name='Sheet1')
#             max_row = df.shape[0]
#             max_column = df.shape[1]



#             class objData:
#                 Account = ''
#                 Group = ''
#                 Post = ''


#             account_data = []

#             for a, b, c in zip(df["Account"], df["Group"], df["Post"]):
#                 obj = objData()

#                 obj.Account = str(a)
#                 obj.Group = str(b)
#                 obj.Post = str(c)

#                 account_data.append(obj)

#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 # driver = connect_driver(i, session)
#                 t2 = threading.Thread(target=post_data, args=(account_data, driver, i,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete create post process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/schedule_sharing_main", methods=["GET", "POST"])
# def schedule_sharing_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             timing = request.form["count_value"]

#         else:
#             return render_template("time_setup_process.html")

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# # That is home page like scrapping tool and scrape the data into given website urls
# @app.route("/edit_proxy_main", methods=["GET", "POST"])
# def edit_proxy_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if request.method=="POST":
#             how_m = request.form["count"]
#             if how_m == "Apply Proxy":
#                 PROXY = "socks5://127.0.0.1:9050"
#                 session["PROXY"] = PROXY
#                 flash("proxy apply successfully")
#                 return redirect(url_for('home', _external=True, _scheme=secure_type))
#             else:
#                 PROXY = None
#                 session["PROXY"] = PROXY
#                 flash("proxy remove successfully")
#                 return redirect(url_for('home', _external=True, _scheme=secure_type))

#         else:
#             return render_template("Proxy_apply_remove.html")

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# @app.route("/apply_proxy", methods=["GET", "POST"])
# def apply_proxy():
#     """
#     That function was register for new user
#     """
#     try:
#         PROXY = "socks5://127.0.0.1:9050"
#         session["PROXY"] = PROXY
#         return "success"

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# @app.route("/remove_proxy", methods=["GET", "POST"])
# def remove_proxy():
#     """
#     That function was register for new user
#     """
#     try:
#         PROXY = None
#         session["PROXY"] = PROXY
#         return "success"

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))


# @app.route("/change_location_main", methods=["GET", "POST"])
# def change_location_main():
#     """
#     That function was register for new user
#     """
#     try:
#         change_tor_exit_node()
#         flash("Location change successfully")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))
        

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))


# @app.route("/accept_requests_main", methods=["GET", "POST"])
# def accept_requests_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 # driver = connect_driver(i, session)
#                 t2 = threading.Thread(target=accepts_requests, args=(driver,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete leave group process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# @app.route("/cancel_requets_main", methods=["GET", "POST"])
# def cancel_requets_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 # driver = connect_driver(i, session)
#                 t2 = threading.Thread(target=delete_requests, args=(driver,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete leave group process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# @app.route("/send_requests_main", methods=["GET", "POST"])
# def send_requests_main():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 # driver = connect_driver(i, session)
#                 t2 = threading.Thread(target=send_requests, args=(driver,))
#                 threads.append(t2)
#                 t2.start()

#             for t in threads:
#                 t.join()
#             flash("Successfully complete leave group process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))

# @app.route("/close_browser", methods=["GET", "POST"])
# def close_browser():
#     """
#     That function was register for new user
#     """
#     try:
#         if session["Range_browser_open"] != None:
#             threads=[]
#             start = int(session["Range_browser_open"].split('-')[0])
#             end = int(session["Range_browser_open"].split('-')[1])
#             for i in range(start, end + 1):
#                 name = "driver_"+str(i)
#                 driver = app.config.get(name, "")
#                 driver.quit()

#             flash("Successfully close all browser")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))
#         else:
#             flash("Please first run create browser and open broswer process")
#             return redirect(url_for('home', _external=True, _scheme=secure_type))

#     except Exception as e:
#         print(e)
#         flash("Please try again.......................................")
#         return redirect(url_for('home', _external=True, _scheme=secure_type))


# def run_server(app):
#     FlaskUI(app=app, server="flask").run()
#     # app.run()

# if __name__ == "__main__":
#     threads = []
#     t2 = threading.Thread(target=schedual_sharing_fun)
#     threads.append(t2)
#     t2.start()

#     t3 = threading.Thread(target=run_server, args=(app,))
#     threads.append(t3)
#     t3.start()
    
for i in range(1,10):
    print(i)