#!/usr/share/apps/konsole/ Python Intrpreter

import os
import time
import datetime
import subprocess
import saleae

main_folder = "/home/michal/Analizator_stanow/Testy_analizatora/"
proc = subprocess.Popen("/home/michal/Analizator_stanow/LogicRunTest/Logic", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
time.sleep(10)
s = saleae.Saleae()
s.set_capture_seconds(30)

for i in range(5):
	current_time = datetime.datetime.now()
	subfolder_name = main_folder + "{:%Y\%m\%d}".format(current_time) 
	print(subfolder_name)

	if not os.path.exists(subfolder_name):
	  os.makedirs(subfolder_name)
	else: 
	  # for each day is created apart folder
	  print("Folder named: " + subfolder_name + " already exist.")

	file_name = subfolder_name + "/{:%H:%M:%S}".format(current_time)
	print ("File name = " + str(file_name))
	s.capture_to_file(file_name)
