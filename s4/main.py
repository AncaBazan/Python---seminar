import numpy as np

a = np.array([1, 2, 3], dtype='int8')

b = np.array([1, 2, 3])

c = np.array([[1, 2, 3], [4, 5, 6]])

d = np.array(
    [
        [
            [1, 2, 3],
            [4, 5, 6]
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ]
    ])

print("A")
print(a)
print(type(a), type(a[0]), a[0])

print("\nB")
print(b)
print(type(b), type(b[0]), b[0])

print("\nC")
print(c)
print(type(c), type(c[0][0]), c[0, 0])

print("\nD")
print(d)
print(type(d), type(d[0][0][0]), d[0, 0, 0])

# dim, shape, size, itemsize, nbytes
print("Dim: ", a.ndim)
print("Shape: ", a.shape)
print("Size: ", a.size)
print("Item size: ", a.itemsize)
print("No. of bytes: ", a.nbytes)

print("C Dim: ", c.ndim)
print("D Dim: ", d.ndim)
print("B Item size: ", b.itemsize)
print("C Shape: ", c.shape)
print("D Shape: ", d.shape)

# operatii pe ndarray
a = np.array([1, 2, 3])
print(a + 2, a - 2, a * 2, a / 2, a // 2, a ** 2)

b = np.array([4, 5, 6])
print(a + b, a - b, a * b, a / b, a // b, a ** b)

# exemple predefinite de ndarray
print("\n")
z = np.zeros((3, 3))
print(z)

print("\n")
o = np.ones((3, 3))
print(o)

print("\n")
f = np.full((3, 5), 1000)
print(f)

print("\n")
i = np.identity(3)
print(i)

print("\n")
r = np.random.rand(2, 2)
print(r)

print("\n")
ri = np.random.randint(-50, 20, (2, 3))
print(ri)
print("\n")

# copy shallow vs deep
a = np.array([1, 2, 3])
b = a
c = a.copy()

b[0] = 20
print(a, b, c)
