from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
row = len(arr)
columns = len(arr[1])
i = 0
while i < row:
    j = 0
    while j < columns:
        s = 0
        for n in range(i, i + 10):
            for b in range(j, j + 10):
                n1 = arr[n][b][0]
                n2 = arr[n][b][1]
                n3 = arr[n][b][2]
                M = int(n1) + int(n2) + int(n3)
                s += M / 3
        s = int(s // 100)
        for n in range(i, i + 10):
            for b in range(j, j + 10):
                arr[n][b][0] = int(s // 50) * 50
                arr[n][b][1] = int(s // 50) * 50
                arr[n][b][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
