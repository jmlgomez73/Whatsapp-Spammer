from selenium import webdriver
import time

def CountDown(t):
	
	while t >= 0: 
		print(t, end='...')
		time.sleep(1)
		t -= 1
	print("")
		
options= webdriver.ChromeOptions()
#Maybe u have to change the path of the Chrome Driver
options.add_argument('--user-data-dir=C:/Users/xxxxx/AppData/Local/Google/Chrome/User Data/Default')
options.add_argument('--profile-directory=Default')

#Get the driver (Maybe u have to change the path of the Chrome Driver)
driverPath = "C:/WINDOWS/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driverPath,options=options)
driver.get('http://web.whatsapp.com')

#Define the name of the target in WhatsApp Web //Insert the target name
target='xxx'
#Define the amount of messages 
count=xxx

while True:
	try:	
		#Wait for the loaded main page
		element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
		#Search for the target and get into the chat
		driver.find_element_by_xpath('//span[@title="{}"]'.format(target)).click()

		#Select the chatbox
		msg1=driver.find_element_by_xpath('//div[@class="_3uMse"]')

		#Initial value of the timer
		start_time = time.time()

		for i in range(count):
			#Write the msg (Change the message)
			msg1.send_keys("xxx {}".format(i))
			#Send the msg
			msg2=driver.find_element_by_xpath('//button[@class="_1U1xa"]').click()

		#get the result of the timer
		elapsed_time = time.time() - start_time
	except Exception:
		continue
	break


print("Elapsed time in the execution of %g messages: %.10f seconds." % (count,elapsed_time))

#Closing countdown
print("Closing this in...")
CountDown(3)
driver.close()
