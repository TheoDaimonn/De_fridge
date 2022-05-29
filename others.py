def adding_statement(value):
    f = open('statement', 'r').readlines()
    if value not in f and value + '\n' not in f:
        m = open('statement', 'w+')
        m.write(''.join(f) + value + '\n')
        m.close()
    else:
        print(value + ' already exists')

def check_statement(id):
    f = open('statement', 'r').readlines()
    for i in f:
        if str(id) in i.split(' '):
            return i.split(' ')[1][:-1:]

def replace_statement(id, final_value):
    f = open('statement', 'r').readlines()
    for i in f:
        if str(id) in i.split(' '):
            f.remove(i)
    t = open('statement', 'w+')
    t.write(''.join(f))
    t.close()
    adding_statement(str(id) + final_value)

def best_of_five(ingr):
    f = open('currentingr.txt', 'r').readline().split('|')
    mass = {}
    for i in f:
        co = 0
        po = len(i)
        for k in ingr:
            if k in i:
                g = list(i)
                g.remove(k)
                co += 1
        mass.setdefault(co/po, i)
    e = mass.keys()
    e1 = []
    for d in e:
        e1.append(float(d))
    if len(e1)>5:
        e1 = sorted(e1)[-5::]
    else:
        e1 = sorted(e1)
    final = []
    for s in e1:
        final.append(mass[s])
    return final

def add_to_cart(id, value):
    co = 0
    t = 1
    f = open('pplfood', 'r').readlines()
    for i in f:
        if str(id) in i.split('|'):
            kek = i[:-1]
            f.remove(i)
            f.remove(['\n'])
            co = 1
            break
    t = open('pplfood', 'w+')
    if co == 0:
        t = open('pplfood', 'w')
        t.write(''.join(f))
        t.write(str(id) +'|' + value + '\n')
        t.close()
    else:
        t = open('pplfood', 'w')
        t.write(''.join(f))
        t.write(kek + '|' + value + '\n')
        t.close()