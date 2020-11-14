a = '자동정렬'
b = '단축키'
c = '컨트롤'
d = '알트'
e = 'L'

print('PyCharm', a, b, ':', c, '+', d, '+', e)

boo = True;
fal = False
print(boo, fal)

print()

a_list = [1, 2, a, b, '파이썬']
print(a_list)
a_list.append('k')
print('a_list : ', a_list)
print('a_list[3] : ', a_list[3])
a_list.append(['사과', '호떡'])
print('a_list[6][1] : ', a_list[6][1])
print(a_list)

print()

a_dict = {'star': 'bucks'}
print(a_dict)
print("a_dict['star'] : ", a_dict['star'])
a_dict['hollys'] = 'coffee'
print(a_dict['hollys'])

people = [['이름', '키', '몸무게'], {'name': 'bob'}, {'height': 180}, {'weight': 70}, {'dic': ['t', 'i', 'o']}]
print('people : ', people)
print('people[0][1] : ', people[0][1])
print("people[1]['name'] : ", people[1]['name'])
print("people[4]['dic'][0] : ", people[4]['dic'][0])

print()

fruits = ['사과', '포도', '귤', '오렌지']
for fruit in fruits:
    print(fruit)
for i in range(0, 5):
    print(i)
count = 0
for fruit in fruits:
    count = count + 1
print('count : ', count)

print()

people_dict = [
    {'name': 'bob', 'age': 29},
    {'name': 'carry', 'age': 61},
    {'name': 'john', 'age': 44},
    {'name': 'smith', 'age': 75},
    {'name': 'ben', 'age': 26}
]

for person in people_dict:
    print(person['name'], person['age'])

print()

for person in people_dict:
    if person['age'] > 30:
        print(person['name'])

print()

txt = 'narafu@gmail.com'
print(txt)
result = txt.replace('gmail', 'naver')
print(result)
result = result.split('@')
print(result)
print(result[1].split('.'))

