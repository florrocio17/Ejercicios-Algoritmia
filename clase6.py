total = 5
vec = [ ] 
i = 0
sumatotal = 0
while i < total:
    n = int(input("Ingrese un número: ")) 
    vec.append(n)
    i = i + 1
    sumatotal = sumatotal + n
    
promedio = sumatotal / total
print(promedio)
x = 0
while x < total: 
    if vec[x] > promedio:
        print(vec[x])  
    x = x + 1