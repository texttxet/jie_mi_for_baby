s = str('afZ_r9VYfScOeO_UL^RWUc')
b = ''
a = 5
for i in s:
	b += chr(ord(i)+a)
	a += 1
print(b)