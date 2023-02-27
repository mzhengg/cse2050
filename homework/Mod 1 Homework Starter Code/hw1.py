import CustomMath as cmth
import math as mth

def func1(arg):
	return (arg + arg)

def func2(arg):
	return (arg - arg)

def f_dif(func1, func2, arg=0.0):
	return func1(arg) - func2(arg)