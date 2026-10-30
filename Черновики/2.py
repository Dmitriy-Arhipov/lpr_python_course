import numpy as np

mn, mx, n = input().split()
mn, mx, n = float(mn), float(mx), int(n)
data = np.array(list(map(float, input().split())))
hist, a = np.histogram(data, bins=n, range=(mn, mx))
ph = (a[:-1] + a[1:]) / 2
res = ph[np.argmax(hist)]
i = np.where(hist > hist[np.argmax(hist)] / 2)[0]
print(f"{res:+1.3f} {a[i[0]] - res:+1.3f} {a[i[-1] + 1] - res:+1.3f}")
