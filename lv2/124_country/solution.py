contry = [1,2,3]

# 진법의 오해를 풀어야 한다.

# 한자리가 늘어날 때마다 1을 빼주어야 한다.

# 예를 들어 십진법에서 4가 ternary_country에서는 11이 된다. 이는 원칙상 1+4로 5가 되야 하기 때문이다.

def ternary_country(n):
    country = [1, 2, 4]
    
    answer =""
    
    while True:
        if n <=0:
            return answer
        
        n -= 1

# str을 해주지 않으면 str인 answer와 더해지지 않아서 type error 발생        
        answer = str(country[n%3]) + answer
        
        n //= 3

print(ternary_country(10))

        

