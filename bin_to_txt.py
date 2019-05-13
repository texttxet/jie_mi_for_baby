import base64
f = open('keyes.txt','r')
f1 = open('keyes1.txt','w')
f1.write(str(base64.b64decode(f.readline())).remove(1))
f.close()
f1.close()