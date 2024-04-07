import sympy

size = 1000
found_sol = False
sol = [0] * size
sol[0] = 1

while found_sol == False:
    sol[0] = sol[0] + 1
    if sympy.isprime(sol[0]):
        continue
    for i in range(1, size):
        if sympy.isprime(sol[i-1] + i):
            break
        sol[i] = sol[i-1] + i
    if sol[-1] != 0:
        found_sol = True

print(sol[0])
print(sol[0:10])
