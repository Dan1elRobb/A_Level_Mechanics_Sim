with open('tw.txt','w') as f:
    for i in range(30):
        f.write('-3' + '\n')
with open('tw.txt','r') as w:
    a = w.readlines()
    for l in a:
        print(int(l.strip()))