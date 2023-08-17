# Arrays

arr = [1, 2, 3]
print(arr)

# Constant time
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)

arr[0] = 15
print(arr)

# O(n)
arr.insert(2, 7)
print(arr)

# Inicializando um array de tamanho 5
arr = [0]*5
print('Inicializado com 5\n', arr)
