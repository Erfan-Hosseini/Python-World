def generate_rug(n):
    if n % 2 == 0:
        return "The number of rows must be odd!"

    rug = []
    center = n // 2
    for i in range(n):
        row = []
        for j in range(n):
            distance = max(abs(i - center), abs(j - center))
            row.append(distance)
        rug.append(row)

    return rug

n = int(input("Please enter the number of rows (n): "))
result = generate_rug(n)
if isinstance(result, str):
    print(result)
else:
    for row in result:
        print(row)

