import sys
filename = sys.argv[1]
f=open(filename, 'r')
file_list=[]
for line in f:
    file_list.append(line)
f.close()
file_list.reverse()
print(file_list)
for i in range(0, len(file_list)):
    print(file_list[i])
