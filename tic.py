from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options

browser = webdriver.Firefox(executable_path="./gecko")

browser.get("https://playtictactoe.org/")
tl = browser.find_element_by_class_name("game")
tl1= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top left']")
tl2= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top']")
tl3= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top right']")
tl4= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square left']")
tl5= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square right']")
tl6= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom left']")
tl7= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom']")
tl8= browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom right']")
p1=0
p2=0
p3=0
p4=0
p5=0
p6=0
p7=0
p8=0

#t1=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top right']/div[@class='o']")

#Class of x or o within each class on completion of each move

def ll():
	global p1, p2, p3, p4, p5, p6, p7, p8

	try:
		t1=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top left']/div[@class='x']")
	except:
		p1=0
	else:
		p1=1

	if p1==0:
		try:
			t1=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top left']/div[@class='o']")
		except:
			p1=0
		else:
			p1=2



	try:
		t2=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top']/div[@class='x']")
	except:
		p2=0
	else:
		p2=1

	if p2==0:
		try:
			t2=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top']/div[@class='o']")
		except:
			p2=0
		else:
			p2=2



	try:
		t3=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top right']/div[@class='x']")
	except:
		p3=0
	else:
		p3=1

	if p3==0:
		try:
			t3=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top right']/div[@class='o']")
		except:
			p3=0
		else:
			p3=2

	

	try:
		t4=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square left']/div[@class='x']")
	except:
		p4=0
	else:
		p4=1

	if p4==0:
		try:
			t4=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square left']/div[@class='o']")
		except:
			p4=0
		else:
			p4=2


	
	try:
		t5=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square right']/div[@class='x']")
	except:
		p5=0
	else:
		p5=1

	if p5==0:
		try:
			t5=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square right']/div[@class='o']")
		except:
			p5=0
		else:
			p5=2



	try:
		t6=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom left']/div[@class='x']")
	except:
		p6=0
	else:
		p6=1

	if p6==0:
		try:
			t6=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom left']/div[@class='o']")
		except:
			p6=0
		else:
			p6=2



	try:
		t7=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom']/div[@class='x']")
	except:
		p7=0
	else:
		p7=1

	if p7==0:
		try:
			t7=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom']/div[@class='o']")
		except:
			p7=0
		else:
			p7=2



	try:
		t8=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom right']/div[@class='x']")
	except:
		p8=0
	else:
		p8=1

	if p8==0:
		try:
			t8=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square bottom right']/div[@class='o']")
		except:
			p8=0
		else:
			p8=2

	print(p1, p2, p3, p4, p5, p6, p7, p8)


#t = browser.find_element_by_class("pass")
#tr   = browser.find_element_by_class("loginbutton")
tl.click()
tl.click()
ll()

if p2==2:
	tl.click()
	tl8.click()
	ll()
	tl.click()
	tl3.click()
	ll()
	tl.click()
	if p5==2:
		tl.click()
		tl6.click()
		ll()
	elif p6==2:
		tl.click()
		tl5.click()
		ll()


elif p4==2:
	tl.click()
	tl8.click()
	ll()
	tl.click()
	tl6.click()
	ll()
	tl.click()
	if p7==2:
		tl.click()
		tl3.click()
		ll()
	elif p3==2:
		tl.click()
		tl7.click()
		ll()

elif p5==2:
	tl.click()
	tl8.click()
	ll()
	tl.click()
	tl6.click()
	ll()
	tl.click()
	if p7==2:
		tl.click()
		tl3.click()
		ll()
	elif p3==2:
		tl.click()
		tl7.click()
		ll()

elif p7==2:
	tl.click()
	tl8.click()
	ll()
	tl.click()
	tl3.click()
	ll()
	if p5==2:
		tl.click()
		tl6.click()
		ll()
	elif p6==2:
		tl.click()
		tl5.click()
		ll()


#tl.click()
#tl1.click()
#ll()

#tl.click()
#tl4.click()
#ll()
#tl.click()

#t1=browser.find_element_by_xpath("//div[@class='game']/div[@class='board']/div[@class='square top left']/div[@class='x']")

#p=t1.is_enabled()
#print(p)