n = int(input("Digite um número: "))
if n > 2:
    print(n)
elif n == 2:
    print(n, " É 2")

elif n == 3 or n == 5:
    print(n, "É 3 ou 5")

if n % 2 == 0 and n % 7 == 0:
    print("n é divisivel por 2 e por 7")
