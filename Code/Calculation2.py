# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 17:26:14 2018

@author: jacob
"""

import math

def calculate(problem):
    m = 0
    loc = 0
    answer = 0
    prob = list(problem)
    length = len(prob)
    while (m < length):
        if (prob[m] == "*"):
            loc = m
            p = 0
            q = loc + 1
            var1 = str(prob[p])
            var2 = str(prob[q])
            while (p < loc - 1):
                if (prob[p + 1] != " "):
                    var1 = var1 + str(prob[p + 1])
                    p = p + 1
                else:
                    p = p + 1
            while (q < length - 1):
                if (prob[q + 1] != " "):
                    var2 = var2 + str(prob[q + 1])
                    q = q + 1
                else:
                    q = q + 1
            answer = float(var1) * float(var2)
            break
        if (prob[m] == "/"):
            loc = m
            p = 0
            q = loc + 1
            var1 = str(prob[p])
            var2 = str(prob[q])
            while (p < loc - 1):
                if (prob[p + 1] != " "):
                    var1 = var1 + str(prob[p + 1])
                    p = p + 1
                else:
                    p = p + 1
            while (q < length - 1):
                if (prob[q + 1] != " "):
                    var2 = var2 + str(prob[q + 1])
                    q = q + 1
                else:
                    q = q + 1
            answer = float(var1) / float(var2)
            break
        if (prob[m] == "+"):
            loc = m
            p = 0
            q = loc + 1
            var1 = str(prob[p])
            var2 = str(prob[q])
            while (p < loc - 1):
                if (prob[p + 1] != " "):
                    var1 = var1 + str(prob[p + 1])
                    p = p + 1
                else:
                    p = p + 1
            while (q < length - 1):
                if (prob[q + 1] != " "):
                    var2 = var2 + str(prob[q + 1])
                    q = q + 1
                else:
                    q = q + 1
            answer = float(var1) + float(var2)
            break
        if (prob[m] == "-"):
            loc = m
            p = 0
            q = loc + 1
            var1 = str(prob[p])
            var2 = str(prob[q])
            while (p < loc - 1):
                if (prob[p + 1] != " "):
                    var1 = var1 + str(prob[p + 1])
                    p = p + 1
                else:
                    p = p + 1
            while (q < length - 1):
                if (prob[q + 1] != " "):
                    var2 = var2 + str(prob[q + 1])
                    q = q + 1
                else:
                    q = q + 1
            answer = float(var1) - float(var2)
            break
        else:
            m = m + 1
    answer = round(answer, 3)
    return answer
        
math_problem = input("Enter problem: ")
calculate(math_problem)
    
    