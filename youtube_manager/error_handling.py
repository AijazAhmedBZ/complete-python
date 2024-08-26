

x = ('Masala', 'lemon', 'ginger')
y = enumerate(x)

print(y)
print(list(y))

file = open('youtube.txt', 'w')

try:
    file.write('Aoa')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Aoa')

