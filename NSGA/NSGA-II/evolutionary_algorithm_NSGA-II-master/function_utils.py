# -*- coding: utf-8 -*-
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random


#目标函数
def Binh_and_Korn(x_list):
    # 0 <= x <=5, 0 <= y <= 3
    x = x_list[0]
    y = x_list[1]
    f1 = 4*pow(x,2) + 4*pow(y,2)#f1=4*x^2+4*y^2
    f2 = pow(x-5,2)+pow(y-5,2)#f2=(x-5)^2+(y-5)^2
    target = [f1,f2]
    return target


#目标函数的约束|用于非支配排序
def Binh_and_Korn_constraints(x_list):
    # 0 <= x <=5, 0 <= y <= 3
    x = x_list[0]
    y = x_list[1]
    g1 = max(0, 25 - pow(x-5,2) - pow(y,2))#y=25-(x-5)^2-y^2
    g2 = max(0, pow(x-8,2)+pow(y+3,2) - 7.7)#y=(x-8)^2+(y+3)^2-7.7
    violation = [g1,g2]
    return violation



def Rastrigrin(x_list):#未使用
    # -30 <= xi <= 30
    # global minimal is at [0,0,..] where value = 0
    x1 = 0.0
    for i,x in enumerate(x_list,1):
        x1 = x1 + x*x - 10*math.cos(2*math.pi*x) + 10
    return x1

def Rosenbrock(x_list):#未使用
    # -30 <= xi <= 30
    # global minimal is at [1,1,..] where value = 0
    x1 = 0.0
    for i in range(0,len(x_list)-1):
        x1 = x1 + 100*(x_list[i]*x_list[i]-x_list[i+1])*(x_list[i]*x_list[i]-x_list[i+1]) +\
             (1-x_list[i])*(1-x_list[i])
    return x1

def Ackley(x_list):
    # -5 <= xi <= 5
    # global minimal is at [0,0,..] where value = 0
    x1 = 0.0
    x2 = 0.0
    for i,x in enumerate(x_list,1):
        x1 = x1 + x*x
        x2 = x2 + math.cos(2*math.pi*x)
    x1 = -0.2*math.sqrt(x1/i)
    x2 = x2/i
    return -20*math.pow(math.e,x1) - math.pow(math.e,x2) + 22.7182818285
    
def Fonseca(x_list):#未使用
    # -4 <= xi <= 4
    s1,s2 = 0.0,0.0
    n = len(x_list)
    for x in x_list :
        s1 = s1 + pow(x-1.0/math.sqrt(float(n)),2.0)
        s2 = s2 + pow(x+1.0/math.sqrt(float(n)),2.0)

    target = []
    target.append(1.0 - math.exp(-s1))
    target.append(1.0 - math.exp(-s2))
    return target

def Kursawe(x_list):#未使用
    # -5 <= xi <= 5, i = 3
    f1,f2 = 0.0,0.0
    for i in range(0,2) :
        f1 = f1 - 10*math.exp(-0.2*math.sqrt(pow(x_list[i],2.0)+pow(x_list[i+1],2.0)))
    for i in range(0,3) :
        f2 = f2 + pow(abs(x_list[i]),0.8) + 5*math.sin(pow(x_list[i],3.0))
    target = [f1,f2]
    return target
    
def Griewank(x_list):#未使用
    # -300 <= xi <= 300
    # global minimal is at [0,0,..] where value = 0
    x1 = 0.0
    x2 = 1.0
    for i,x in enumerate(x_list,1):
        x1 = x1 + x*x
        x2 = x2 * math.cos(x/math.sqrt(i))
    return x1/4000 - x2 + 1

if __name__ == '__main__':  
    linear_range = 2
    alpha = random.uniform(0, linear_range)
    print(alpha)

