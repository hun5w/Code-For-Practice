#if语句
#矩阵初始化
#链表推导式

#杨辉三角
def yanghui_triangle(n):
    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]

            row.extend([last_row[j]+last_row[j + 1] for j in range(len(last_row) - 1)])
            row.append(1)
        triangle.append(row)

    for row in triangle:
        print(" " * (n))