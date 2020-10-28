###_1
import random
x = []
k = []
for i in range(74):
    x.append(random.randint(1,200))
print(x)

for j in range(1,len(x)):
    if j %2 == 0 and x[j]%2 != 0:
        k.append(x[j])
print(k)

###_2
import random
x = []
k = []
for i in range(77):
    x.append(random.randint(1,200))
print(x)

for j in range(1,len(x)):
    if j %3 == 0 and x[j]%2 == 0:
        k.append(x[j])
print(k)

##_3
import random
x = []
k = []
for i in range(71):
    x.append(random.randint(1,200))
print(x)

for j in range(1,len(x)):
    if j %2 == 0 and x[j] < 0:
        print("1")
        break
    else:
        print("0")
        break
        

###_4
import random
x = []
k = []
for i in range(80):
    x.append(random.randint(1,200))
print(x)

for j in range(1,len(x)):
    if j %3 == 0 and x[j] < 0:
        print("1")
        break
    else:
        print("0")
        break





##_5
import random

print("სწორია თუ არა, რომ x მასივში არ არის არც ერთი ისეთი ელემენტი, რომლის მნიშვნელობა უარყოფითია?")
x = []
k = []
for i in range(83):
    x.append(random.randint(1,200))
# print(x)

for j in range(1,len(x)):
    if  x[j] < 0:
        print("არ არის სწორი.")
        break
    else:
        print("დიახ, სწორია.")
        break

##_6
import random

x = []
k = []
for i in range(86):
    x.append(random.randint(1,200))
print(x)
for j in range(len(x)):
    if   j %3 ==0 and x[j] %2 == 0:
        # k.append(x[j])
        print(1)
        break
    else:
        print(0)
        break





