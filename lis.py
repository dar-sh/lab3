from graphics import *
from pylab import *
import scipy as sc
import numpy as np

p=arange (0.0, 1, 0.01)
y=(p*1j)**7+5*(p*1j)**6+7*(p*1j)**3+(p*1j)+1
s=real(y)
r=imag(y)
plot(s,r,linewidth=0.7)
xlabel("Real")
ylabel("Imagine")
grid(True)
show()

t=arange(0.0, 20*pi, 0.05)
s=cos(t)
r=cos(t + pi/2)
p=plot(s,r,linewidth=0.3)
grid(True)
show()

t=arange(0.0, 20*pi, 0.05)
s=cos(3*t)
r=cos(5*t - pi/2)
p=plot(s,r,linewidth=0.3)
grid(True)
show()

t=arange(0.0, 10*pi, 0.05)
s=cos(5*t)
r=cos(7*t + pi/2)
p=plot(s,r,linewidth=0.3)
grid(True)
show()

t=arange(0.0, 50*pi, 0.05)
s=cos(3*t*pi)
r=cos(4*t + pi/2)
p=plot(s,r,linewidth=0.3)
grid(True)
show()

t=arange(0.0, 20*pi, 0.01)
s=cos(t)
r=cos(6*t)
p=plot(s,r,linewidth=0.3)
title('Chebyshev')
grid(True)
show()

t=arange(0.0, 20*pi, 0.01)
s=sin(6*t)
r=sin(t)
p=plot(s,r,linewidth=0.3)
title('Chebyshev 2')
grid(True)
show()
