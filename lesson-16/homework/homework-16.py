1)
import numpy as np

arr = np.arange(1, 11)
squared = arr ** 2


total = np.sum(squared)
mean = np.mean(squared)
std_dev = np.std(squared)

print("Original array:", arr)
print("Squared array:", squared)
print("Sum:", total)
print("Mean:", mean)
print("Standard Deviation:", std_dev)

exercises

51)
Z = np.zeros(10, dtype=[('position', [('x', float), ('y', float)]),
                        ('color', [('r', float), ('g', float), ('b', float)])])
print(Z)
52) Z = np.random.rand(100, 2)
dist = np.sqrt(np.sum((Z[:, np.newaxis, :] - Z[np.newaxis, :, :])**2, axis=-1))
print(dist)
53)
Z = np.arange(10, dtype=np.float32)
Z = Z.astype(np.int32, copy=False)
print(Z)
54)
from io import StringIO
data = StringIO("1, 2, 3, 4, 5\n6,  ,  , 7, 8\n ,  , 9,10,11")
Z = np.genfromtxt(data, delimiter=",")
print(Z)
55)
Z = np.arange(9).reshape(3, 3)
for index, value in np.ndenumerate(Z):
    print(index, value)
57)n = 10  # rows
m = 10  # columns
p = 20  # number of elements

Z = np.zeros((n, m))
indices = np.random.choice(n * m, p, replace=False)
Z[np.unravel_index(indices, (n, m))] = 1
print(Z)
58)X = np.random.rand(5, 10)
Y = X - X.mean(axis=1, keepdims=True)
print(Y)
59)Z = np.random.randint(0, 100, (5, 5))
print("Original:\n", Z)
Z_sorted = Z[Z[:, 2].argsort()]  # sort by column index 2
print("Sorted by 3rd column:\n", Z_sorted)
60) Z = np.random.randint(0, 2, (5, 10))
Z[:, 3] = 0  # force a null column
null_columns = ~Z.any(axis=0)
print("Null columns found:", null_columns)
61) Z = np.random.uniform(0, 100, 10)
target = 50
index = (np.abs(Z - target)).argmin()
print("Array:", Z)
print("Nearest to", target, ":", Z[index])
62) A = np.arange(3).reshape(1, 3)
B = np.arange(3).reshape(3, 1)
for x, y in np.nditer([A, B], flags=['external_loop'], op_flags=['readonly']):
    print(x + y)
64) Z = np.zeros(10)
indices = [1, 1, 3, 5, 3]
np.add.at(Z, indices, 1)
print(Z)
65) X = np.array([1, 2, 3, 4, 5])
I = np.array([0, 1, 2, 1, 0])
F = np.zeros(3)
np.add.at(F, I, X)
print(F)  
66) 
image = np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)
unique_colors = np.unique(image.reshape(-1, 3), axis=0)
print("Unique colors:", len(unique_colors))
67) A = np.random.rand(2, 3, 4, 5)
result = A.sum(axis=(-2, -1))
print(result.shape)  # Should be (2, 3)
68) D = np.array([1, 2, 3, 4, 5, 6])
S = np.array([0, 1, 0, 1, 0, 1])

means = [D[S == i].mean() for i in np.unique(S)]
print("Means by subset:", means)
69) A = np.random.rand(5, 5)
B = np.random.rand(5, 5)
diag = np.sum(A * B.T, axis=1)
print("Diagonal of dot product:", diag)

70) Z = np.array([1, 2, 3, 4, 5])
R = np.zeros(len(Z) + (len(Z)-1)*3, dtype=int)
R[::4] = Z
print("Interleaved:", R)
71) A = np.ones((5, 5, 3))
B = 2 * np.ones((5, 5))
result = A * B[:, :, np.newaxis] 
print(result.shape)  
72)Z = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
Z[[0, 1]] = Z[[1, 0]]
print(Z)
73)
triangles = np.random.randint(0, 10, (10, 3))
edges = np.sort(np.vstack([triangles[:, [0, 1]],
                           triangles[:, [1, 2]],
                           triangles[:, [2, 0]]]), axis=1)
unique_edges = np.unique(edges, axis=0)
print(unique_edges)
74) 
C = np.array([0, 3, 1])
A = np.repeat(np.arange(len(C)), C)
print(A)  # A = [1, 1, 1, 2]

75) def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

Z = np.arange(10)
print(moving_average(Z, n=3))
76)
Z = np.arange(10)
shape = (Z.size - 2, 3)
strides = (Z.strides[0], Z.strides[0])
windows = np.lib.stride_tricks.as_strided(Z, shape=shape, strides=strides)
print(windows)
77)

Z = np.array([True, False, True])
Z = ~Z
print(Z)

Z = np.array([1.0, -2.0, 3.0])
Z *= -1
print(Z)
78)
P0 = np.random.rand(10, 2)
P1 = np.random.rand(10, 2)
p = np.random.rand(2)

d = np.abs(np.cross(P1 - P0, P0 - p)) / np.linalg.norm(P1 - P0, axis=1)
print(d)
79)
 P0 = np.random.rand(5, 2)
P1 = np.random.rand(5, 2)
P = np.random.rand(10, 2)

d = np.abs(np.cross(P1 - P0, P0[:, None] - P)) / np.linalg.norm(P1 - P0, axis=1)[:, None]
print(d)  # Shape: (5, 10)

81)
Z = np.arange(1, 15)
R = np.lib.stride_tricks.sliding_window_view(Z, window_shape=4)
print(R)
82) Z = np.random.rand(10, 10)
rank = np.linalg.matrix_rank(Z)
print("Rank:", rank)
83)
Z = np.random.randint(0, 10, 50)
vals, counts = np.unique(Z, return_counts=True)
most_freq = vals[np.argmax(counts)]
print("Most frequent:", most_freq)
84) Z = np.random.rand(10, 10)
blocks = np.lib.stride_tricks.sliding_window_view(Z, (3, 3))
print(blocks.shape) 
86) p, n = 3, 2
matrices = np.random.rand(p, n, n)
vectors = np.random.rand(p, n, 1)

result = np.sum(np.matmul(matrices, vectors), axis=0)
print(result.shape)  
87)
Z = np.random.rand(16, 16)
reshaped = Z.reshape(4, 4, 4, 4)
block_sum = reshaped.sum(axis=(2, 3))
print(block_sum.shape)  # (4, 4)
88) Z = np.random.rand(16, 16)
reshaped = Z.reshape(4, 4, 4, 4)
block_sum = reshaped.sum(axis=(2, 3))
print(block_sum.shape)  # (4, 4)
89) Z = np.random.rand(100)
n = 5
largest = Z[np.argpartition(Z, -n)[-n:]]
print(np.sort(largest)[::-1])
 90) import itertools

arrays = [np.array([1, 2]), np.array([3, 4])]
product = np.array(list(itertools.product(*arrays)))
print(product)
92)Z = np.arange(1, 11)

# Method 1
print(Z ** 3)

# Method 2
print(np.power(Z, 3))

# Method 3
print(np.multiply(Z, np.multiply(Z, Z)))

93) A = np.random.randint(0, 5, (8, 3))
B = np.random.randint(0, 5, (2, 2))

mask = np.array([np.any(np.all(np.isin(a, b)) for b in B) for a in A])
result = A[mask]
print("A:\n", A)
print("Rows of A containing elements from rows in B:\n", result)
94)Z = np.random.randint(0, 5, (10, 3))
unique_rows = Z[~(Z[:,0] == Z[:,1]) | ~(Z[:,1] == Z[:,2])]
print("Original:\n", Z)
print("Unequal rows:\n", unique_rows)
95)
Z = np.array([0, 1, 2, 3, 4, 5, 6, 7])
binary_matrix = ((Z[:, None] & (1 << np.arange(8))) > 0).astype(int)
print(binary_matrix)
96) Z = np.random.randint(0, 2, (10, 3))
unique_rows = np.unique(Z, axis=0)
print("Unique rows:\n", unique_rows)
99)
X = np.random.randint(0, 5, (10, 5))
n = 10
valid_rows = X[np.sum(X, axis=1) == n]
print("Valid rows:\n", valid_rows)
100)
X = np.random.rand(1000)
N = 1000
samples = np.random.choice(X, (N, len(X)), replace=True)
means = samples.mean(axis=1)
ci = np.percentile(means, [2.5, 97.5])
print("95% Confidence Interval:", ci)










