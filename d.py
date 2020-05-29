k = ''
with open('f.txt', mode='rb') as a:
    v = a.read()
    for i in v:
        if i % 3 == 0 and i % 5 != 0:
            k += str(i)+''
b = open('g.txt', mode='w')
b.write(k)
b.close()
with open('g.txt') as b:
    print(b.read())
