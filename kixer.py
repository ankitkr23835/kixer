import time
xed=input('your file name:')
dex=int(input('your character size:'))
a="abcdefghijklmnopqrstuvwxyz1234567890!@#$%^,:;?/_-(){}%"
#for 1 digit passwords
start = time.time()
if dex == 1:
        for z in a:
                print(z, file=open(xed, "a"))
#for 2 digit  passwords
if dex == 2:
        for z in a:
                for y in a:
                        print(z,y, sep="", file=open(xed, "a"))
#for 3 digit  passwords
if dex == 3:
        for z in a:
                for y in a:
                        for x in a:
                                print(z,y,x, sep="", file=open(xed, "a"))
#for 4 digit passwords
if dex == 4:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        print(z,y,x,w, sep="", file=open(xed, "a"))
#for 5 digit passwords
if dex == 5:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                print(z,y,x,w,v, sep="", file=open(xed, "a"))
#for 6 digit passwords
if dex == 6:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                for u in a:
                                                        print(z,y,x,w,v,u, sep="", file=open(xed, "a"))
#for 7 digit passwords
if dex == 7:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                for u in a:
                                                        for t in a:
                                                        	print(z,y,x,w,v,u,t, sep="", file=open(xed, "a"))   
#for 8 digit passwords
if dex == 8:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                for u in a:
                                                        for t in a:
                                                                for s in a:
                                                                        print(z,y,x,w,v,u,t,s, sep="", file=open(xed, "a"))                                                     
#for 9 digit passwords
if dex == 9:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                for u in a:
                                                        for t in a:
                                                                for s in a:
                                                                        for r in a:
                                                                                print(z,y,x,w,v,u,t,s,r, sep="", file=open(xed, "a"))                                           
#for 10 digit passwords
if dex == 10:
        for z in a:
                for y in a:
                        for x in a:
                                for w in a:
                                        for v in a:
                                                for u in a:
                                                        for t in a:
                                                                for s in a:
                                                                        for r in a:
                                                                                print(z,y,x,w,v,u,t,s,r,q, sep="", file=open(xed, "a"))
end = time.time()                                                                                
print('password generated successfully as', xed)                                                                               
print(end-start)
                                                                
