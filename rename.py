import os, sys, glob

for i, imgname in enumerate(glob.iglob('*.*')):
	ext = imgname.split('.')[1]
	if not (ext == 'txt' or ext == 'py'):
		# print(ext)
		temp = imgname.split('.')[0].split(' ')
		# if i > 2:break
		# print(imgname)
		# print(os.path.basename(imgname).split('.')[0])
		
		
		namelist = [temp[0], temp[-1], ' '.join(temp[1:-1]) + '.' + ext]
		print(' '.join(namelist))
		# temp = 'test02.txt'
		os.rename(imgname, ' '.join(namelist))