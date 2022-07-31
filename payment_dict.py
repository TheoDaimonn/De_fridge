from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime
import random
import time

QIWI_PRIV_KEY = 'eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InYyZG5lbi0wMCIsInVzZXJfaWQiOiI3OTEzMzkyMzg4NCIsInNlY3JldCI6IjRmNTgzYzc4ODcwNjZhNmMzMTBjYzJmNmUzZWQ5OWUxOTFhNjkwNWQyNDIwNTUyNmQwYTFmM2NlZjgwMDRjMGUifX0='
p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
def create_de_trans(id):
    # Выставим счет на сумму 228 рублей который будет работать 45 минут
    idd = random.randint(1, 10000)
    new_bill = p2p.bill(bill_id=idd, amount=50, lifetime=45)
    m = ''.join(open('pays', 'r', encoding='utf-8').readlines())
    t = open('pays', 'w+', encoding='utf-8')
    t.write(m + str(id) + '\t' + str(idd) + '\n')
    t.close()
    return new_bill.pay_url

def check_status(id):
    y = open('pays', 'r', encoding='utf-8').readlines()
    for p in y:
        if str(id) in p.split('\t'):
            idd = p.split('\t')[1][:-1:]
            ms = p
            break
    stat = p2p.check(bill_id=int(idd)).status
    if stat != 'WAITING':
        y.remove(ms)
        k = open('pays','w', encoding='utf-8')
        k.write(''.join(y))
    return stat
    #WAITING/PAID
def clearr(id, db):
    try:
        y = open(db, 'r', encoding='utf-8').readlines()
        for p in y:
            if str(id) in p.split('\t'):
                y.remove(p)
                break
        k = open(db, 'w', encoding='utf-8')
        k.write(''.join(y))
    except Exception:
        pass