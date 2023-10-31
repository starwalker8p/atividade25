soma=0
for num in range(1,7):
    numero=(int(input(f"{num} numero: ")))
    if numero % 2 == 0:
        soma+=numero
print(f"a soma é {soma}")