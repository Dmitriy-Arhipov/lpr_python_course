import numpy as np

seed, n, p, m = input().split()
seed, n, m = map(int, [seed, n, m])
p = float(p)
np.random.seed(seed)
diff = []
for i in range(m+1):
    diff.append(n)
    o = (n*np.random.binomial(1, p,n).mean()).astype(int)
    n = o
diff = [abs(diff[i]-diff[i-1])/diff[i-1] for i in range(1, m+1)]
print(' '.join(map(lambda x: f'{x:.3f}', diff)))

