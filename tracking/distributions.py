###############################################################################
#                                                                             #
#   Distribution functions code                                               #
#   Code written by Dawith Lim                                                #
#                                                                             #
#   Version: 1.0.0                                                            #
#   First written on 2020/08/05                                               #
#   Last modified: 2021/12/24                                                 #
#                                                                             # 
#   Supporting file with different distribution functions that are used in    #
#   the ant data processing codebase                                          #
#                                                                             #
#   Packages used                                                             #
#                                                                             #
###############################################################################

import numpy as np

def gaussian1D(x, mean, amplitude, sigma):
# Returns the probability of obtaining x from a Gaussian distribution
    return amplitude * np.exp(-((x-mean)/sigma)**2)

def laplace1D(x, mu, b):
# Returns the probability of obtaining x from a Laplace distribution
    return np.exp(-np.abs(x-mu)/b)/(2*b)

def laplaceasym1D(x, mu, b, k):
# Returns the probability of obtaining x from an asymmetric Laplace
# distribution
    clone = x
    clone[x<mu] = np.exp(b*(x[x<mu]-mu)/k)/(2*b)
    clone[x>=mu] = np.exp(-b*k*(x[x>=mu]-mu)) 
    print(clone)
    return clone

def logistic1D(x, mu, s):
# Returns the probability of obtaining x from a logistic distribution
    return np.exp(-(x-mu)/s)/(s*(1+np.exp(-(x-mu)/s))**2)

def lorentz1D(x, mean, amplitude, gamma):
# Returns the probability of obtaining x from a Lorentz distribution
    return amplitude / (1 + ((x - mean) / gamma)**2)

def polyo2(x, a1, a2, c):
# Returns a second order polynomial function a1*x^2 + a2*x + c
    return a1 * x**2 + a2 * x + c

def vonMises1D(x, mu, k):
# Returns the probability of obtaining x from a Von Mises distribution
    return np.exp(k*np.cos(x-mu))/(2*np.pi*modbessel(0,k))

def composite_lorentz_polyo2(x, a1, a2, c, mu, b, gamma):
# Linear sum of 2O polynomial and Lorentz distribution
    return polyo2(x,a1,a2,c) + lorentz1D(x,mu,b,gamma)

def composite_lorentz_polyo1(x, a1, c, mu, b, gamma):
# Linear sum of 1O polynomial and Lorentz distribution
    return a1*x + lorentz1D(x,mu,b,gamma)
