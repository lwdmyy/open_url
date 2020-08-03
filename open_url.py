import re
import os
import sys
import time


PACKAGE_NAME = "com.baidu.searchbox"
ACTIVITY_NAME = "com.baidu.searchbox.MainActivity"
def main(filename):
	with open(filename,'r') as f :
		for i in f :
			i = i.strip()
			os.system('adb shell am start -n ' + PACKAGE_NAME +'/' + ACTIVITY_NAME + ' -a android.intent.action.VIEW -d ' + i  + '')
			time.sleep(5)
			os.system('adb shell input swipe 540 1300 540 500 500')
			time.sleep(1)
			os.system('adb shell input swipe 540 500 540 1300 500')
			time.sleep(5)		

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: python3 run.py filename')
		sys.exit()
	filename = sys.argv[1]
	main(filename)

	# for filename in os.listdir('urls'):
	# 	if len(re.findall('.txt',filename)) > 0:
	# 		main('urls/'+filename)
			
				