import time
from selenium import webdriver
import os
import re
import traceback
import sys
driver=None
def visit(broswer):
	global driver
	if 'chrome' == broswer.lower():

		driver=webdriver.Chrome()
	elif 'firefox' == broswer.lower():
		driver=webdriver.Firefox()
	else:
		driver=webdriver.Ie()

def get(url):
	global driver
	driver.get(url)

def input(location,word):
	global driver
	driver.find_element_by_xpath(location).send_keys(word)

def click(location):
	global driver
	driver.find_element_by_xpath(location).click()
def sleep(s):
	time.sleep(s)

def assert_word(expect_word):
	global driver
	try:
		assert expect_word in driver.page_source
		print("%s校验成功"%expect_word)
	except Exception as e:
		print("校验失败",e)
		traceback.print_exc()
	driver.quit()
def read_file(file):

	if os.path.exists(file):
		data_list=[]
		with open(file,'r',encoding='utf-8') as fp:
			for line in fp:
				data_list.append(line.strip())
		return data_list
	else:
		print("%s文件不存在"%file)
		sys.exit(0)

datas=read_file('data.txt')
for data in datas:
	data=eval(data)
	keywords=read_file('keyword.txt')
	for keyword in keywords:
		if '{{' in keyword:
			key=re.search(r'{{(.*?)}}',keyword).group(1)
			keyword=re.sub(r'{{(%s)}}'%key,data[key],keyword)
		#print(keyword)
		if keyword.count('||')==0:
			command=keyword
		elif keyword.count('||')==2:
			function,location,word=keyword.split('||')
			command='%s(\"%s\",\"%s\")'%(function,location,word)
		elif keyword.count('||')==1:
			function,location=keyword.split('||')
			if function!='sleep':
				command='%s(\"%s\")'%(function,location)
			else:
				command='%s(%s)'%(function,location)
		#print(command)
		try:
			eval(command)
		except:
			print("用例执行失败%s"%command)


# visit('Chrome')
# get('http://baidu.com')
# input('//input[@id="kw"]','python')
# click('//input[@id="su"]')
# sleep(1)
# assert_word('hhhhhhh')

	