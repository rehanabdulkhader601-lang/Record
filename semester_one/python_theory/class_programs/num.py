import numpy as np

# Array creation methods

r = np.zeros((2, 3))
print(r)

u = np.ones(4)
print(u)

p = np.eye(3)
print(p)

m = np.arange(0, 10, 2)
print(m)

k = np.linspace(0, 1, 5)
print(k)


# Creating arrays

a = np.array([1, 2, 3, 4])
print(a)

b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)

c = np.array([1, 2, 3], dtype=float)
print(c)

x = np.array([1, 2.5, 3])
print(x)


# Array properties

g = b.ndim
print(g)

i = b.shape
print(i)

o = b.size
print(o)

print(b.ndim)  # Dimension

q = b.dtype
print(q)

l = b.itemsize
print(l)


# One-dimensional array operations

p = np.array([1, 2, 3])
v = np.array([4, 5, 6])

print(p + v)  # Addition of one-dimensional matrix
print(p - v)  # Subtraction of one-dimensional matrix
print(p * v)  # Scalar multiplication of one-dimensional matrix


# Two-dimensional array operations

first = np.array([[2, 3, 5],
                  [4, 5, 6]])

second = np.array([[8, 7, 9],
                   [6, 9, 7]])

print(first + second)  # Addition of 2-dimensional matrix
print(second - first)  # Subtraction of 2-dimensional matrix
print(first * second)  # Multiplication of 2-dimensional matrix
print(first * second)


# Additional two-dimensional array operation

first1 = np.array([[2, 3],
                   [4, 5],
                   [9, 0]])

second1 = np.array([[8, 7],
                    [6, 9],
                    [6, 5]])

print(first1 * second1)
