import requests
from bs4 import BeautifulSoup
#typ = open('set.txt','r',encoding='utf-8').readline().split('&')
#for y in typ:
    #try:
url = 'https://povar.ru/recipes/kokteil_kosmopoliten-4811.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

title = str(soup.find_all('h1')).split('>')[1].split('<')[0]
print(str(title))


img = soup.find_all(itemprop='image')
img = str(img).split('src="')[1]
n = ''
for i in img:
    n+= i
    if n[-3::] == 'jpg':
        break
img = n
print(str(img))





ingr_names = str(soup.find_all(itemprop="recipeIngredient")).split('</li>')
s = []
nam = []
for i in ingr_names:
    print(i)
    try:

        n = i.split('>')[1]
        nam.append(n.split('  ')[0])
        s.append(n)
    except Exception:
        pass
ingr_names = s
print(ingr_names)
print(nam)

exit()

reciepe = str(soup.find(type='text'))
reciepe = reciepe.split('</li>')[0]
print(reciepe)

exit()


img_data = requests.get('https://amwine.ru'+img).content
with open(f'{title}.jpg', 'wb+') as handler:
    handler.write(img_data)
    handler.close()
with open(f'{title}', 'w+', encoding='utf-8') as f:
    f.write(title + '\n')
    for k in range(len(ingr_names)):
        f.write(ingr_names[k] + ingr_values[k] + '\n')
    f.write('\n')
    f.write('\n'.join(headline))
    f.close()
op = open('currentingr.txt', 'r',encoding='utf-8').readline().split('|')
sm = open('currentingr.txt', 'w+', encoding='utf-8')
for u in ingr_names:
    if u not in op:
        op.append(u)
sm.write('|'.join(op))
sm.close()

ik = open('recepies+ingr', 'r', encoding='utf-8').readlines()
t = open('recepies+ingr', 'w+', encoding='utf-8')
ik.append(title + '%'+'%'.join(ingr_names)+ '\n')
t.write(''.join(ik))
t.close()


print(title)
print(img)
print(ingr_names)
print(ingr_values)
print(headline)
    #except Exception:
     #   pass