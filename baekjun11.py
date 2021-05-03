a = int(input())
b = input()

for i in range(0, 3):
    result = a*int(b[2-i])
    print(result)
 
print(a*int(b))