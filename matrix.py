def identify(matrix):
    if matrix[0][0] == 1 and matrix[1][1] == 1 and matrix[0][1] == 0 and matrix[1][0] == 0:
        print("Its an identity matrix")

    elif matrix[0][0] == matrix[1][1] and matrix[0][1] == 0 and matrix[1][0] == 0:
        print("Its a scalar matrix")

    if matrix[1][0] == 0:
        print("Its an upper triangular matrix")

    if matrix[0][1] == 0:
        print("Its a lower triangular matrix")


def main():
    print("Enter matrix 1")
    m1 = []

    for i in range(2):
        row = input().split()
        row[0] = int(row[0])
        row[1] = int(row[1])
        m1.append(row)

    print("Enter matrix 2")
    m2 = []

    for i in range(2):
        row = input().split()
        row[0] = int(row[0])
        row[1] = int(row[1])
        m2.append(row)

    print("Matrix 1 result:")
    identify(m1)

    print("Matrix 2 result:")
    identify(m2)


if __name__ == "__main__":
    main()