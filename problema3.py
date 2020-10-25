#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.  
x=0
s=0
while not((x%2!=0) and (x%3==0)):
    x=eval(input('Introduceti un numar'))
    if x%2==0:
        s+=x
print('Suma tuturor numerelor pare introdusse est', s)