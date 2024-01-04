


a = [1,3,3,3,3,3,2]


def clone(a):
    r = []
    for i in a:
        r.append(i)
    return r
with open('mot.txt') as e:
    lines =e.readlines()
line = []
for i in range(len(lines)):
    lines[i] = lines[i].replace('\n','')
    if len(lines[i])==5 and "'"not in lines[i]:
        line.append(lines[i])
print(line)
alph = "abcdefghijklmnopqrstuvwxyz"

state = [0]*26

for i in range(5):
    ban = ""
    pcor = ""
    cor = ['.'] * 5
    inr = input()#e,0:r,1:r,2:
    j = inr.split(':')
    js = 0
    for i in j :
        h = i.split(',')
        print(h)
        if(h[1] == '0'):
            ban+=h[0]
        elif(h[1] == '1'):
            pcor+=h[0]
        else:
            cor[js] = h[0]
        js+=1
    print(ban)
    print(pcor)
    print(cor)

    c = clone(line)
    for i in c:
        t = 0
        print(i)
        r = False
        for j in i:
            print(j)
            if j in ban or (j != cor[t] and '.' != cor[t]):
                line.remove(i)
                break
            t+=1

    print(line)



#a,0:d,1:i,0:e,2:u,0