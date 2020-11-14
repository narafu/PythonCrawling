print('Hello sparta')
a = 3
b = a
a = a + 1

# --------------------------------------------------

num = a * b
name = 'bob'

# --------------------------------------------------

a_list = []
a_list.append(1)
a_list.append([2, 3])
print(a_list)
print(a_list[1])

# ---------------------------------------------------

a_dict = {}
a_dict = {'name': 'bob', 'age': 21}
a_dict['height'] = 178
print(a_dict)
print(a_dict['name'])

# ---------------------------------------------------

people = [{'name': 'bob'}, {'age': 21}]
people.append('사랑')
print(people)

# ---------------------------------------------------

fruits = ['사과', '배', '포도']
for fruit in fruits:
    print(fruit)

# ---------------------------------------------------

people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 38}, {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17}, {'name': 'ben', 'age': 27}]

for person in people:
    print(person['name'], person['age'])

for person in people:
    if person['age'] > 20:
        print(person['name'])

# ---------------------------------------------------

txt = 'sprta@gmail.com'
result1 = txt.split('@')
print(result1)

result2 = txt.split('@')[1].split('.')
print(result2)

result3 = result2[0].replace('g', 'naver')
print(result3)

# ---------------------------------------------------

