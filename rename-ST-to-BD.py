import os, sys, glob, shutil

if len(sys.argv) < 2:
	print('parameter required')
	exit(1)
	

for i, fullname in enumerate(glob.iglob(os.path.join(sys.argv[1], '*.*'))):
	try:
		# if i > 2:break
		print(fullname)

		filename, ext = os.path.splitext(os.path.basename(fullname))
		if not (type(int(filename[0:14])) == int and filename[14] == '_'): continue

		year = filename[0:4]
		month = filename[4:6]
		day = filename[6:8]
		hh = filename[8:10]
		mm = filename[10:12]
		ss = filename[12:14]
		# print(year, month, day, hh, mm, ss)
		outname = '-'.join([year, month, day + ' ' + hh, mm, ss, '000' + ext])
		print(outname)
		shutil.copy2(fullname, os.path.join(sys.argv[1], outname))

	except Exception as e:
		print(e)
		
		
		
		# print(imgname)
		# print(os.path.basename(imgname).split('.')[0])