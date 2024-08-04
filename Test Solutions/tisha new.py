def partition_oranges(n, diameters):
    k = 0
    pivot = diameters[-1]

    for i in range(n-1):
        if diameters[i] <= pivot:
            diameters[i], diameters[k] = diameters[k], diameters[i]
            k += 1

    diameters[k], diameters[-1] = diameters[-1], diameters[k]

    return diameters

n = int(input("Enter the number of oranges tisha pluced from orchard: "))
diameters = []
for i in range(n):
    diameter = int(input(f"Enter the diameter of orange {i+1}: "))
    diameters.append(diameter)

result = partition_oranges(n, diameters)
print(result)