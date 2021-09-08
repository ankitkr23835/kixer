xed=input('your file name:')
dex=int(input('your character size:'))
a="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^,:;?/_-(){}%"
for z in a:
	for y in a:
		for x in a:
			for w in a:
				if dex == 1:
					print(z, file=open(xed, "a"))
				elif dex == 2:
					print(z,y, sep="", file=open(xed, "a"))
				elif dex == 3:
					print(z,y,x, sep="", file=open(xed, "a"))
