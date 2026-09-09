# Program 107: Spiral number matrix (4x4)
#  1   2   3   4
# 12  13  14   5
# 11  16  15   6
# 10   9   8   7
def generate_spiral(n):
    matrix = [[0] * n for _ in range(n)]
    top, bottom, left, right = 0, n - 1, 0, n - 1
    val = 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            matrix[top][c] = val
            val += 1
        top += 1
        for r in range(top, bottom + 1):
            matrix[r][right] = val
            val += 1
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                matrix[bottom][c] = val
                val += 1
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                matrix[r][left] = val
                val += 1
            left += 1
    return matrix

def main():
    try:
        n = int(input("Enter matrix dimension n (e.g. 4): "))
        matrix = generate_spiral(n)
        for row in matrix:
            print(" ".join(f"{x:3d}" for x in row))
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
