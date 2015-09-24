import os
from os.path import isfile, join,isdir

files = []
path = '/home/renjith/ann/djswap/'

def search_files(path):
	if isdir(path):
		print "searching ...."
		for f in os.listdir(path):
			if isfile(join(path, f)):
				path_f = path + f
				files.append(path_f)
			else:
				temp_path = join(path,f) +"/"
				temp_file = search_files(temp_path)
	return files

file_list = search_files(path)

print file_list



