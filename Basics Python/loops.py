n=int(input("Enter a number of your choice: "))

print(f"Print numbers not divisible by 3 between 1 and {n} are :")
for i in range(1, n+1):
    if(i%3)==0:
        continue
    print(i)