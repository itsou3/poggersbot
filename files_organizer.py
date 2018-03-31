#Creates a textfile in each subdir with list of all files/subdirs within
#Also creates a folder in parent dir and copies all text files to folder

import os
import shutil
import time 

time = time.ctime()
path = os.walk(".")
newdir = "__LISTS__"	#name of new directory

# Makes new directory if directory does not exist
if not os.path.exists(newdir):
	os.makedirs(newdir)

try: 
	for Dir, subDir, filenames in path:
		for subdirectory in subDir:
			if subdirectory == "__LISTS__":	# Don't make a list for the new created directory
				pass
			else:
				here = os.path.dirname(os.path.realpath(__file__))		# Sets the subdirectory as path
				name = "___ " + subdirectory + " list.txt"		# name of textfile to be created
				filepath = os.path.join(here, subdirectory, name)		# textfile is created
				files_in_subdir = os.listdir(subdirectory)		# dir list
				with open(filepath, "w") as f:
					f.write("Created on ")
					f.write(time)
					f.write("\n" * 3)

					for each_file in files_in_subdir:
						if "list.txt" in each_file:
							pass
						else:
							f.write(each_file)
							f.write("\n")
				try:
					shutil.copy(filepath, newdir)
				except shutil.Error:
					pass
except WindowsError:
	pass

print "done"