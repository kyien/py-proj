#File handling in pyhton

#syntax

#file object=open(path_to_file,access_type/mode)

#modes r,r+,rb,w,w+,wb,a,a+

#file attributes:file.mode,file.closed,file.name

#Example 1
#names_list=['James','Yvonne','Matthew','Janet']
#fo=open('lists.txt','w+')
#for name in names_list:
	#fo.write(str(name)+'\n')

#fo.close()

#Example 2
fo=open('names.txt','r+')
names=[]
line=fo.readline()
while line:
	if line.endswith('\n'):
		print(line.strip('\\n'))
		#names.append(line)
		#print(line)
	else:
		names.append(line)

	line=fo.readline()
fo.close()

print(names)


