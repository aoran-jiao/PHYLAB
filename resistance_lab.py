import math
import matplotlib.pyplot as plt

data = [[0.088, 6.19], [0.279, 6.18], [0.733, 6.18], [3.28, 6.18]] # x, y data sets

'''
# option 1
xl = [0.088, 0.279, 0.733, 3.28]
yl = [6.19, 6.18, 6.18, 6.18]
'''

# option 2

xl = [0.089, 0.279, 0.733, 3.27]
yl = [6.18, 6.15, 6.11, 5.86]


### linear fit
N = len(data)

sum_x_sq = sum(x**2 for x in xl)
delta = N*sum_x_sq - sum(xl)**2
xy = [xl[i]*yl[i] for i in range(N)]

m = (N*sum(xy) - sum(xl)*sum(yl)) / delta
b = (sum(yl) - m*sum(xl)) / N

varl = [ (yl[i] - (b + m*xl[i]) ) ** 2 for i in range(N)]
variance = sum(varl) / (N - 2)

sm = math.sqrt(N*variance/delta)
sb = math.sqrt(variance*sum_x_sq/delta)

print("slope =", m, "+-", sm)
print('y-int =', b, '+-', sb)

### chi-squared test
def f(x, m, b):
  return m*x + b

un_y = 0.005 # uncertainty for V is 0.005V
chi_l = [ ( yl[i] - f(xl[i], m, b) )**2 / un_y**2 for i in range(N)]

de_free = N - 2 # degree of freedom = N - # parameters
chi_sq = sum(chi_l)
reduced_chi_sq  = chi_sq/de_free # should be around 1 for good fit

print('Chi-squared = ', chi_sq, 'Reduced chi_sq = ', reduced_chi_sq)


### Residuals Graph
y_predicted = [f(x, m, b) for x in xl]
residual = [yl[i] - y_predicted[i] for i in range(N)]

print('Residual = ', residual)

plt.scatter(xl, residual, label="stars", color="green",
            marker="1", s=30)

plt.xlabel('I')
plt.ylabel('Residual V')

plt.title('Residual Graph of V vs I')

# plt.show()
plt.savefig('graph2.png')


