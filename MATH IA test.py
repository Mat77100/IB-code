import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x**2) #exp puts to the power of e

x = np.linspace(0,2,10000) # x axis from 0 to 1, with 1000 uniform steps inbetween
y = f(x) # y value of x at that point (both are arrays, so this is an array of each y value)

plt.plot(x,y)
'''
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of $e^{-x^2}$")
plt.show()
'''
#Estimation = np.trapezoid(y,x)
#print(Estimation)

a = 0
b = 2
n = 1000000


def LCG(seed,a,c,m,n):
    numbers = []
    for i in range(n):
        seed = (a*seed + c) % m
        numbers.append(seed/m) #makes values between 0 and 1, which is where we're integrating
    return numbers


def MeanIntegrate(Samples,a,b,n):
    return (b-a)/n * np.sum(f(Samples))



Samples = np.array(LCG(222, 1809, 8387, 2**26, n))
Samples = a + (b-a)*Samples


Estimate = MeanIntegrate(Samples,a,b,n)
print(f"Samples: {n}")
print(Estimate)

plt.scatter(Samples,f(Samples),color="red",s=15, marker="P",linestyle='None',label="Monte Carlo sample points")
plt.plot(x,y,label="$e^{-x^2}$", color="black")
plt.title("Genarated x-values plotted on the line of $e^{-x^2}$")
plt.legend()
plt.figtext(0.3,0.01,r"$\int_{0}^{2}e^{-x^{2}}\ dx\ \approx $"+f"{Estimate}")
plt.show()
