#Find the root of f(x) = 2(x^3) - 11.7(x^2) + 17.7(x) - 5
#using Newton-Rhapson method
#with the error tolerance 0.05%

x = [3] #list to keep the x value for each iteration
i = 0 #current iteration
e = 1 #the error

while e >= 0.05:
    fx = 2*x[i]*x[i]*x[i] - 11.7*x[i]*x[i] + 17.7*x[i] - 5
    ddx_fx = 6*x[i]*x[i] - 23.4*x[i] + 17.7
    x.append(x[i]-fx/ddx_fx)
    i += 1

    e = abs((x[i]-x[i-1])/x[i])*100

print(x[i])