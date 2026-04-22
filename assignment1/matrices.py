def main():
    
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    
    m1 = []
    print("Enter elements of Matrix1:")
    for i in range(rows):
        row = list(map(int, input().split()))
        m1.append(row)

    m2 = []
    print("Enter elements of Matrix2:")
    for i in range(rows):
        row = list(map(int, input().split()))
        m2.append(row)

    
    print("\nMatrix Addition Result:")
    add = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(m1[i][j] + m2[i][j])
        add.append(row)

    for r in add:
        print(r)


    print("\nMatrix Multiplication Result:")
    mul = []
    for i in range(rows):
        row = []
        for j in range(cols):
            total = 0
            for k in range(cols):
                total += m1[i][k] * m2[k][j]
            row.append(total)
        mul.append(row)

    for r in mul:
        print(r)


main()