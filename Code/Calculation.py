# -*- coding: utf-8 -*-

def calculate(problem):
    ans = list(problem)
    m = 0
    while(m < len(ans)):
        if (m != 0):
            if (ans[m] == "+"):
                try:
                    while(m + 2 < len(ans)):
                        ans[m + 1] = float(str(ans[m + 1]) + str(ans[m + 2]))
                        del ans[m + 2]
                except ValueError:
                    ans[m + 1] = ans[m + 1]    
                ans[m - 1] = float(ans[m - 1]) + float(ans[m + 1])
                del ans[m]
                del ans[m]
            elif (ans[m] == "-"):
                try:
                    while(m + 2 < len(ans)):
                        ans[m + 1] = float(str(ans[m + 1]) + str(ans[m + 2]))
                        del ans[m + 2]
                except ValueError:
                    ans[m + 1] = ans[m + 1]     
                ans[m - 1] = float(ans[m - 1]) - float(ans[m + 1])
                del ans[m]
                del ans[m]
            elif (ans[m] == "*"):
                try:
                    while(m + 2 < len(ans)):
                        ans[m + 1] = float(str(ans[m + 1]) + str(ans[m + 2]))
                        del ans[m + 2]
                except ValueError:
                    ans[m + 1] = ans[m + 1]     
                ans[m - 1] = float(ans[m - 1]) * float(ans[m + 1])
                del ans[m]
                del ans[m]
            elif (ans[m] == "/"):
                try:
                    while(m + 2 < len(ans)):
                        ans[m + 1] = float(str(ans[m + 1]) + str(ans[m + 2]))
                        del ans[m + 2]
                except ValueError:
                    ans[m + 1] = ans[m + 1]     
                ans[m - 1] = float(ans[m - 1]) / float(ans[m + 1])
                del ans[m]
                del ans[m]
            
            else:
                ans[m - 1] = float(str(ans[m - 1]) + str(ans[m]))
                del ans[m]
        else:
            m = m + 1
    finalanswer = str(ans[0])
    print (finalanswer)
    
math_problem = input("Enter problem: ")
calculate(math_problem)

