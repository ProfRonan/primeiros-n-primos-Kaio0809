n = int(input("Digite um número: "))
print("2")
primo = 1
prox_primo = 3
while primo < n:
    x = 3
    while(x < prox_primo):
        if prox_primo % x == 0:
            break
        x = x + 2
    if x == prox_primo:
        print(x)
        primo = primo + 1
    prox_primo = prox_primo + 2