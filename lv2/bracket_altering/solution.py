p1 = "(()())()"

p2 = ")("

p3 = "()))((()"

############ 틀린 문제 풀이 #######################

def solution(p):
    R = 0
    L = 0
    incorrect = 0
    
    answer = ""
    
    for i in range(len(p)):
        if p[i] == ")":
            L += 1
            if L > R:
                incorrect += 1
                answer += "("
            else:
                answer += p[i]
                
        else:
            if incorrect == 0:
                R += 1
                answer += p[i]  

            elif incorrect > 0:
                incorrect -= 1
                R += 1
                answer += ")"
            
    return answer
    
    
print(solution(p3))

############# 