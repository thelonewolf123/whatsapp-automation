#!/usr/bin/python3

import sys
import pandas as pd

from termcolor import colored
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from time import sleep


message = "Hello It's automated text testing."

if(len(sys.argv) == 2):

	browser  = webdriver.Chrome()
	browser.get('https://web.whatsapp.com/')
	#wait for qr-code scan
	input('Press enter after scanning the qr-code')
	#find element and send text

	data = pd.read_csv(sys.argv[1])
	name 	 = pd.DataFrame(data,columns=['Name']).values.tolist()
	#print(contacts)

	for item in name:
		
		searchbox = browser.find_element_by_class_name('selectable-text')
		searchbox.send_keys(item)
		sleep(3)
		
		try:
			
			elmn = browser.find_element_by_xpath(f'//span[@title = "{item[0]}" ]')
			elmn.click()
			inputBox = browser.find_element_by_class_name('_3u328')
			inputBox.send_keys(f'{message}\n') 
			text = colored(f'Whatsapp message has been sent for {item[0]}','green')
			print(text)
			#sendtext = browser.find_element_by_class_name('_3M-N-')
			#sendtext.click()
			sleep(3)
		
		except Exception:
			#print('Error')
			text = colored(f'Whatsapp account is not available for {item[0]}','red')
			print(text)
		
		searchbox.send_keys(Keys.CONTROL,'a')
		searchbox.send_keys(Keys.BACKSPACE)

else:
	text = colored(f'Usage : {sys.argv[0]} /path/to/file.csv','red')
	print(text)
