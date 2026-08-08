X = [50, 60, 70, 80, 90, 100]
y = [500, 600, 700, 800, 900, 1000]

n = len(X)
mean_x = sum(X) / n
mean_y = sum(y) / n

num = 0  
den = 0  

for i in range(n):
    num += (X[i] - mean_x) * (y[i] - mean_y)
    den += (X[i] - mean_x) ** 2

w = num / den

b = mean_y - w * mean_x

metraj = 75
price = w * metraj + b
print(f"خونه {metraj} متری ≈ {price:.0f} میلیون")
