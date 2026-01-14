o = open('1.txt', 'r')
w = open('2.txt', 'w')

for line in o:
	w.write(line)

o.close()
w.close()